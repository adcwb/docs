### 一、 核心流程与原理解析



为了精准统计 SQL 在 MySQL 服务端的实际执行耗时（排除网络传输和 Go 客户端 GC/调度 耗时），我们采用了 **“独占连接 + 顺序执行 + 历史回溯”** 的方案。



#### 1. 连接池与独占连接 (`sql.DB` vs `sql.Conn`)



- **`db *sql.DB` (连接池):** 这是一个对象池。当你调用 `db.Query` 时，它会随机从池中拿一个空闲连接，用完立即放回。**不能**用于本场景，因为我们必须保证后续的操作都在**同一个 TCP 连接**上。
- **`db.Conn(ctx)` (独占连接):**
  - **动作：** 从连接池中“借出”一个物理连接，并将其锁定。
  - **状态：** 在你调用 `conn.Close()` 归还之前，这个连接**永远**属于当前 Goroutine，不会被其他协程抢占。



#### 2. 获取身份 (`THREAD_ID`)



- **操作：** `SELECT THREAD_ID FROM performance_schema.threads WHERE PROCESSLIST_ID = CONNECTION_ID();`
- **状态变化：**
  - SQL 发送 -> MySQL 执行 -> 返回结果 -> **连接依然被 `conn` 对象持有**。
  - **注意：** 此时连接**没有**归还给连接池，但对于这个 `conn` 对象而言，当前处于“空闲/Ready”状态，可以执行下一条 SQL。



#### 3. 执行业务 SQL (核心耗时点)



- **操作：** `rows, _ := conn.QueryContext(ctx, "SELECT ...")`
- **状态变化：** 连接进入 **"Busy" (忙碌)** 状态。MySQL 服务端开始计算、查询，并将结果集放入网络缓冲区等待发送。



#### 4. 读取数据与释放语句 (`rows.Close`)



- **操作：** `rows.Scan` 读取数据，最后必须调用 `rows.Close()`。
- **为什么要显式 Close？**
  - 在 MySQL 协议中，**同一个连接是串行的**。如果上一条 SQL 的结果集还没读完（或者没 Close），连接缓冲区里还有残留数据，客户端就不能发送新的 SQL（比如查 PFS）。
  - `rows.Close()` 的作用是：告诉驱动程序“我读完了，你可以清空缓冲区了”，将 `conn` 的状态从 **"Busy"** 重置为 **"Idle"**。
  - **关键点：** 此时连接**依然没有**归还给 `db` 连接池，它还在我们手里，准备执行第三步。



#### 5. 回溯历史 (`performance_schema`)



- **操作：** `SELECT ... FROM events_statements_history WHERE THREAD_ID = ? AND SQL_TEXT IS NOT NULL `
- **状态变化：** 复用同一个连接，发送这条查询。
- **为什么能查到？**
  - 因为步骤 3 的业务 SQL 刚刚执行完毕并 Close 了，MySQL 内核会自动将那条语句的执行信息（开始时间、结束时间、SQL文本）“归档”写入到当前 Thread 的历史表中。
  - 我们现在去查，就是在查“刚刚发生的历史”。

示例SQL

```mysql
SELECT 
    CAST(FORMAT((TIMER_END - TIMER_START) / 1000000000, 6) AS DECIMAL(20, 6))
FROM performance_schema.events_statements_history
WHERE THREAD_ID = ? 
  AND SQL_TEXT IS NOT NULL
ORDER BY EVENT_ID DESC 
LIMIT 1
```





#### 6. 归还连接



- **操作：** `defer conn.Close()`
- **状态变化：** 物理连接被释放，重新回到 `db *sql.DB` 连接池中，等待被其他 Goroutine 复用。此时该 Thread ID 在 MySQL 内部可能会被解绑或销毁。

------



### 二、 核心术语百科





#### 1. Performance Schema (PFS)



- **定义：** MySQL 的一个内置存储引擎（从 MySQL 5.5 开始引入，5.7/8.0 默认开启）。
- **用途：** 它像一个植入在 MySQL 内核中的“黑匣子”，用于实时监控服务器的运行细节（锁、IO、内存、SQL 执行等）。
- **特点：** 极低损耗，数据保存在内存中，重启后丢失。



#### 2. `events_statements_history` 表



- **定义：** 记录了最近执行的 SQL 语句的历史事件表，线程释放后该表相关记录会被清空。
- **存储结构：** **环形缓冲区 (Ring Buffer)**。
- **容量限制：** 默认每个线程只保留最近的 **10条** 记录。
- **挤出机制：** 当第 11 条 SQL 执行时，第 1 条记录会被覆盖。这就是为什么我们必须在执行完业务 SQL 后**立刻**查询的原因。



#### 3. `THREAD_ID` vs `PROCESSLIST_ID`



- **`PROCESSLIST_ID` (Connection ID):** 也就是 `SHOW PROCESSLIST` 里的 ID。这是面向客户端的会话 ID（例如：连接号 123）。
- **`THREAD_ID`:** 这是 Performance Schema 内部使用的、唯一的内核线程 ID（例如：线程号 456）。
- **关系：** 是一一对应的，但数值不同。PFS 表几乎都使用 `THREAD_ID` 作为主键或索引。



#### 4. 时间单位：皮秒 (ps) 与 毫秒 (ms)



- MySQL PFS 底层计时器 (`TIMER_START`, `TIMER_END`) 使用 **皮秒 (Picoseconds)**。
- **换算公式：**
  - 1 毫秒 (ms)  == 1000 微秒 (μs)
  - 1 微秒 (μs)  ==  1000 纳秒 (ns)
  - 1 纳秒 (ns)  == 1000 皮秒 (ps)
  - 1 皮秒 (ps)  ==  1000 飞秒 (fs)
  - 1 飞秒 (fs)  ==  1000 阿秒 (as)
  - 1 阿秒 (as) ==  1000 仄秒 (zs)
- **代码换算：**
  - 如果只除以 $10^6$，得到的是 **微秒**。
  - 要得到 **毫秒**，必须除以 **$10^9$ (`1000000000`)**。

------



### 三、 深度释疑：为什么 `ORDER BY DESC` 能保证精准？



**“在同一个连接里，怎么保证我查到的那条就是刚才执行的业务 SQL，而不是别的？”**



这得益于 **TCP 连接的串行性** 和 **过滤条件的排他性**。

让我们看一个时间轴（Timeline）：

1. **T1:** `conn.Query("SELECT THREAD_ID ...")`
   - MySQL 执行完毕。PFS 历史表写入记录 A。
2. **T2:** `conn.Query("SELECT * FROM users ...")` (**业务 SQL**)
   - MySQL 执行完毕。PFS 历史表写入记录 B。
   - **此时，记录 B 是该 Thread 最新的记录。**
3. **T3:** `conn.Query("SELECT ... FROM history ...")` (**查询 PFS 的 SQL**)
   - 这条 SQL 正在**运行中**，通常**不会**立即出现在 `history` 表中（或者我们在查询中排除了自身）。

**我们的查询逻辑是：**

SQL

```
SELECT ... FROM history 
WHERE THREAD_ID = ? 
  AND SQL_TEXT IS NOT NULL   -- 排除 com_prepare 等无文本事件
ORDER BY EVENT_ID DESC       -- 倒序（最新的在最上面）
LIMIT 1
```

**为什么是准确的？**

1. **连接独占：** 因为使用了 `db.Conn()`，在 T1 到 T3 期间，**没有任何其他协程**能在这个连接上插入 SQL。
2. **过滤干扰：** 我们过滤掉了 `SQL_TEXT IS NULL` 的事件（如 `Prepare`, `Execute` 等底层命令）。
3. **时间顺序：** 在 T3 时刻去查历史，T2（业务 SQL）一定是**已经完成的、最近一条**有文本的记录。T1（查 ID）虽然也在，但它的 `EVENT_ID` 比 T2 小，会被 `ORDER BY DESC` 排到后面去。

**总结：** 只要连接不被复用、不被并发插入，**“倒序取第一条”** 在逻辑上就是绝对准确的。



