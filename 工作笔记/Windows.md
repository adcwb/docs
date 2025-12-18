### 端口占用



查找所有运行的端口

```cmd
netstat -ano
```



查看被占用端口对应的PID

```cmd
netstat -aon|findstr "8888"
```



查看指定PID的进程

```cmd
tasklist|findstr "PID"
```



结束进程

强制（/F参数）杀死 pid 为 9088 的所有进程包括子进程（/T参数）

```cmd
taskkill /T /F /PID 9088
```

