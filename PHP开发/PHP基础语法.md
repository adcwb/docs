## PHP基础语法



[toc]

### PHP简介

#### 什么是 PHP

- PHP 是 "PHP Hypertext Preprocessor" 的首字母缩略词
- PHP 是一种被广泛使用的开源脚本语言
- PHP 脚本在服务器上执行
- PHP 没有成本，可供免费下载和使用



#### 什么是 PHP 文件

- PHP 文件能够包含文本、HTML、CSS 以及 PHP 代码
- PHP 代码在服务器上执行，而结果以纯文本返回浏览器
- PHP 文件的后缀是 ".php"



#### PHP 能够做什么

- PHP 能够生成动态页面内容
- PHP 能够创建、打开、读取、写入、删除以及关闭服务器上的文件
- PHP 能够接收表单数据
- PHP 能够发送并取回 cookies
- PHP 能够添加、删除、修改数据库中的数据
- PHP 能够限制用户访问网站中的某些页面
- PHP 能够对数据进行加密

通过 PHP，您可以不受限于只输出 HTML。您还能够输出图像、PDF 文件、甚至 Flash 影片。您也可以输出任何文本，比如 XHTML 和 XML。



#### 为什么使用 PHP

- PHP 运行于各种平台（Windows, Linux, Unix, Mac OS X 等等）
- PHP 兼容几乎所有服务器（Apache, IIS 等等）
- PHP 支持多种数据库
- PHP 是免费的。请从官方 PHP 资源下载：[www.php.net](http://www.php.net/)
- PHP 易于学习，并可高效地运行在服务器端



### PHP安装

如需开始使用 PHP，您可以：

- 使用支持 PHP 和 MySQL 的 web 主机
- 在您的 PC 上安装 web 服务器，然后安装 PHP 和 MySQL。



#### 使用支持 PHP 的 Web 主机

如果您的服务器支持 PHP，那么您无需做任何事情。

只要创建 .php 文件，然后上传到 web 目录中即可。服务器会自动对它们进行解析。

您无需编译或安装任何额外的工具。

因为 PHP 是免费的，大多数 web 主机都支持 PHP。



#### 在您的 PC 上运行 PHP

不过如果您的服务器不支持 PHP，那么您必须：

- 安装 web 服务器
- 安装 PHP
- 安装数据库，比如 MySQL

官方的 PHP 网站 (PHP.net) 提供了 PHP 的安装说明：http://php.net/manual/zh/install.php



### PHP基本语法

#### hello

```php+HTML
<!DOCTYPE html>
<html>
<body>

<h1>我的第一张 PHP 页面</h1>

<?php
	echo "Hello PHP!";
?>  

</body>
</html>

```



#### 基础PHP语法

PHP 脚本可放置于文档中的任何位置。

PHP 脚本以 *<?php* 开头，以 *?>* 结尾：

PHP 文件的默认文件扩展名是 ".php"。

PHP 文件通常包含 HTML 标签以及一些 PHP 脚本代码。

**注意：**PHP 语句以分号结尾（;）。PHP 代码块的关闭标签也会自动表明分号（因此在 PHP 代码块的最后一行不必使用分号）。

```php
<?php
	// 此处是 PHP 代码
?>
```



#### 注释

PHP 代码中的注释不会被作为程序来读取和执行。它唯一的作用是供代码编辑者阅读。

注释用于：

- 使其他人理解您正在做的工作 - 注释可以让其他程序员了解您在每个步骤进行的工作（如果您供职于团队）
- 提醒自己做过什么 - 大多数程序员都曾经历过一两年后对项目进行返工，然后不得不重新考虑他们做过的事情。注释可以记录您在写代码时的思路。

单行注释：

```php
<?php
    // 这是单行注释
	# 这也是单行注释
?>
```

多行注释：

```php
<?php
    /*
        这是多行注释块
        它横跨了多行
    */
?>
```



#### PHP 大小写敏感

在 PHP 中，所有用户定义的函数、类和关键词（例如 if、else、echo 等等）都对大小写不敏感。

在下面的例子中，所有这三条 echo 语句都是合法的（等价）：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
    ECHO "Hello PHP!<br>";
    echo "Hello PHP!<br>";
    EcHo "Hello PHP!<br>";
?>

</body>
</html>
```

在 PHP 中，所有变量都对大小写敏感

在下面的例子中，只有第一条语句会显示 $color 变量的值（这是因为 $color、$COLOR 以及 $coLOR 被视作三个不同的变量）：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
    $color="red";
    echo "My car is " . $color . "<br>";
    echo "My house is " . $COLOR . "<br>";
    echo "My boat is " . $coLOR . "<br>";
?>

</body>
</html>
```

#### 变量

什么是变量：

​	变量是存储信息的容器

PHP 变量规则：

- 变量以 $ 符号开头，其后是变量的名称
- 变量名称必须以字母或下划线开头
- 变量名称不能以数字开头
- 变量名称只能包含字母数字字符和下划线（A-z、0-9 以及 _）
- 变量名称对大小写敏感（$y 与 $Y 是两个不同的变量）

**注意：**PHP 变量名称对大小写敏感！

PHP 没有创建变量的命令。变量会在首次为其赋值时被创建

```php+HTML
<?php
    $txt="Hello world!";
    $x=5;
    $y=10.5;
?>
```

以上语句执行后，变量 txt 会保存值 Hello world!，变量 x 会保存值 5，变量 y 会保存值 10.5。

**注意：**如果您为变量赋的值是文本，请用引号包围该值。



**PHP 是一门类型松散的语言**

在上面的例子中，请注意我们不必告知 PHP 变量的数据类型。

PHP 根据它的值，自动把变量转换为正确的数据类型。

在诸如 C 和 C++ 以及 Java 之类的语言中，程序员必须在使用变量之前声明它的名称和类型。



**变量的作用域**

在 PHP 中，可以在脚本的任意位置对变量进行声明。

变量的作用域指的是变量能够被引用/使用的那部分脚本。

PHP 有三种不同的变量作用域：

- local（局部）
- global（全局）
- static（静态）

**Local 和 Global 作用域**

函数之外声明的变量拥有 Global 作用域，只能在函数以外进行访问。

函数内部声明的变量拥有 LOCAL 作用域，只能在函数内部进行访问。

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
$x=5; // global scope
  
function myTest() {
   $y=10; // local scope
   echo "<p>在函数内部测试变量：</p>";
   echo "变量 x 是：$x";
   echo "<br>";
   echo "变量 y 是：$y";
} 

myTest();

echo "<p>在函数之外测试变量：</p>";
echo "变量 x 是：$x";
echo "<br>";
echo "变量 y 是：$y";
?>

</body>
</html>
```

​	在上例中，有两个变量 $x 和 $y，以及一个函数 myTest()。$x 是全局变量，因为它是在函数之外声明的，而 $y 是局部变量，因为它是在函数内声明的。

​	如果我们在 myTest() 函数内部输出两个变量的值，$y 会输出在本地声明的值，但是无法 $x 的值，因为它在函数之外创建。

​	然后，如果在 myTest() 函数之外输出两个变量的值，那么会输出 $x 的值，但是不会输出 $y 的值，因为它是局部变量，并且在 myTest() 内部创建。

**注意：**您可以在不同的函数中创建名称相同的局部变量，因为局部变量只能被在其中创建它的函数识别。

#####  global关键字

global 关键词用于在函数内访问全局变量。

要做到这一点，请在（函数内部）变量前面使用 global 关键词：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
    $x=5;
    $y=10;

    function myTest() {
       global $x,$y;
       $y=$x+$y;
    } 

    myTest(); // 运行函数
    echo $y; // 输出变量 $y 的新值
?>

</body>
</html>

```

PHP 同时在名为 $GLOBALS[index] 的数组中存储了所有的全局变量。下标存有变量名。这个数组在函数内也可以访问，并能够用于直接更新全局变量。

上面的例子可以这样重写：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
$x=5;
$y=10;

function myTest() {
   $GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y'];
} 

myTest();
echo $y;
?>

</body>
</html>

```

##### static 关键字

​	通常，当函数完成/执行后，会删除所有变量。

​	不过，有时需要不删除某个局部变量。实现这一点需要更进一步的工作。

​	要完成这一点，请在您首次声明变量时使用 *static* 关键词：

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
function myTest() {
   static $x=0;
   echo $x;
   $x++;
}

    myTest();
    echo "<br>";
    myTest();
    echo "<br>";
    myTest();
    echo "<br>";
    myTest();
    echo "<br>";
    myTest();
?>  

</body>
</html>

```

然后，每当函数被调用时，这个变量所存储的信息都是函数最后一次被调用时所包含的信息。

**注意：**该变量仍然是函数的局部变量。



#### echo 和 print

echo 和 print 之间的差异：

- echo - 能够输出一个以上的字符串

​		echo 是一个语言结构，有无括号均可使用：echo 或 echo()。

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
    echo "<h2>PHP 很有趣！</h2>";
    echo "Hello world!<br>";
    echo "我计划学习 PHP！<br>";
    echo "这段话", "由", "多个", "字符串", "串接而成。";
?>  

</body>
</html>

```

- print - 只能输出一个字符串，并始终返回 1

​		print 也是语言结构，有无括号均可使用：print 或 print()。

```php+HTML
<!DOCTYPE html>
<html>
<body>

<?php
    print "<h2>PHP is fun!</h2>";
    print "Hello world!<br>";
    print "I'm about to learn PHP!";
?>  

</body>
</html>

```



**注意：**echo 比 print 稍快，因为它不返回任何值。



#### 数据类型

##### 字符串

字符串是字符序列，比如 "Hello world!"。

字符串可以是引号内的任何文本。您可以使用单引号或双引号：

```php
<?php 
    $x = "Hello world!";
    echo $x;
    echo "<br>"; 
    $x = 'Hello world!';
    echo $x;
?>
```

##### 整型

整数是没有小数的数字。

整数规则：

- 整数必须有至少一个数字（0-9）
- 整数不能包含逗号或空格
- 整数不能有小数点
- 整数正负均可
- 可以用三种格式规定整数：十进制、十六进制（前缀是 0x）或八进制（前缀是 0）

在下面的例子中，我们将测试不同的数字。PHP var_dump() 会返回变量的数据类型和值：

```php
<?php 
    $x = 5985;
    var_dump($x);
    echo "<br>"; 
    $x = -345; // 负数
    var_dump($x);
    echo "<br>"; 
    $x = 0x8C; // 十六进制数
    var_dump($x);
    echo "<br>";
    $x = 047; // 八进制数
    var_dump($x);
?>
```

##### 浮点型

浮点数是有小数点或指数形式的数字。

在下面的例子中，我们将测试不同的数字。PHP var_dump() 会返回变量的数据类型和值：

```php
<?php 
    $x = 10.365;
    var_dump($x);
    echo "<br>"; 
    $x = 2.4e3;
    var_dump($x);
    echo "<br>"; 
    $x = 8E-5;
    var_dump($x);
?>
```

##### 数组

略



##### 对象

对象是存储数据和有关如何处理数据的信息的数据类型。

在 PHP 中，必须明确地声明对象。

首先我们必须声明对象的类。对此，我们使用 class 关键词。类是包含属性和方法的结构。

key 可以是 integer 或者 string。value 可以是任意类型。

此外 key 会有如下的强制转换：

- String 中包含有效的十进制 int，除非数字前面有一个 `+` 号，否则将被转换为 int 类型。例如键名 `"8"` 实际会被储存为 `8`。另外， `"08"` 不会被强制转换，因为它不是一个有效的十进制整数。
- Float 也会被转换为 int ，意味着其小数部分会被舍去。例如键名 `8.7` 实际会被储存为 `8`。
- Bool 也会被转换成 int。即键名 `true` 实际会被储存为 `1` 而键名 `false` 会被储存为 `0`。
- Null 会被转换为空字符串，即键名 `null` 实际会被储存为 `""`。
- Array 和 object *不能* 被用为键名。坚持这么做会导致警告：`Illegal offset type`。

如果在数组定义时多个元素都使用相同键名，那么只有最后一个会被使用，其它的元素都会被覆盖。

然后我们在对象类中定义数据类型，然后在该类的实例中使用此数据类型：

```php
<?php
class foo {
    function test() {
        echo "object test!";
    }
}

$a = new foo;
$a->test();

?>

```

##### 逻辑

逻辑是 true 或 false。

```php
$x=true;
$y=false;
```

逻辑常用于条件测试。您将在本教程稍后的章节学到更多有关条件测试的知识。

##### NULL

特殊的 NULL 值表示变量无值。NULL 是数据类型 NULL 唯一可能的值。

NULL 值标示变量是否为空。也用于区分空字符串与空值数据库。

可以通过把值设置为 NULL，将变量清空：

```php
<?php
    $x="Hello world!";
    $x=null;
    var_dump($x);
?>
```



#### 字符串函数

PHP 字符串函数是 PHP 核心的组成部分。无需安装即可使用这些函数。

|       函数       |                             类型                             |                             示例                             |
| :--------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|     strlen()     |                  返回字符串的长度，以字符计                  |                 echo strlen("Hello world!");                 |
| str_word_count() |                      统计字符串中单词数                      |            echo str_word_count("a b"); // 输出 2             |
|     strrev()     |                          字符串反转                          |                echo strrev("ab"); // 输出 ba                 |
|     strpos()     | 检索字符串内指定的字符或文本; 如果找到匹配，则会返回首个匹配的字符位置。如果未找到匹配，则将返回 FALSE |             echo strpos("Hello world!","world");             |
|  str_replace()   |             用一些字符串替换字符串中的另一些字符             | echo str_replace("world", "Kitty", "Hello world!"); // 输出 Hello Kitty! |



#### 常量

常量是单个值的标识符（名称）。在脚本中无法改变该值。

有效的常量名以字符或下划线开头（常量名称前面没有 $ 符号）。

常量是自动全局的，而且可以贯穿整个脚本使用。

**注意：**与变量不同，常量贯穿整个脚本是自动全局的。



如需设置常量，请使用 define() 函数 - 它使用三个参数：

1. 首个参数定义常量的名称
2. 第二个参数定义常量的值
3. 可选的第三个参数规定常量名是否对大小写不敏感。默认是 false。

下例创建了一个*对大小写敏感的常量*，值为 "Welcome to W3School.com.cn!"：

```php
<?php
    define("GREETING", "Welcome to www.baidu.com!");
    echo GREETING;
?>
```



#### 运算符

##### 算数运算符

| 运算符 | 名称 | 例子    | 结果            |
| :----- | :--- | :------ | :-------------- |
| +      | 加法 | $x + $y | $x 与 $y 求和   |
| -      | 减法 | $x - $y | $x 与 $y 的差数 |
| *      | 乘法 | $x * $y | $x 与 $y 的乘积 |
| /      | 除法 | $x / $y | $x 与 $y 的商数 |
| %      | 取模 | $x % $y | $x 除 $y 的余数 |

```php
<?php 
    $x=17; 
    $y=8;
    echo ($x + $y); // 输出 25
    echo ($x - $y); // 输出 9
    echo ($x * $y); // 输出 136
    echo ($x / $y); // 输出 2.125
    echo ($x % $y); // 输出 1
?>
```

##### 赋值运算符

PHP 赋值运算符用于向变量写值。

PHP 中基础的赋值运算符是 "="。这意味着右侧赋值表达式会为左侧运算数设置值。

|  赋值  |  等同于   |              描述              |
| :----: | :-------: | :----------------------------: |
| x = y  |   x = y   | 右侧表达式为左侧运算数设置值。 |
| x += y | x = x + y |               加               |
| x -= y | x = x - y |               减               |
| x *= y | x = x * y |               乘               |
| x /= y | x = x / y |               除               |
| x %= y | x = x % y |              模数              |

```php
<?php 
    $x=17; 
    echo $x; // 输出 17

    $y=17; 
    $y += 8;
    echo $y; // 输出 25

    $z=17;
    $z -= 8;
    echo $z; // 输出 9

    $i=17;
    $i *= 8;
    echo $i; // 输出 136

    $j=17;
    $j /= 8;
    echo $j; // 输出 2.125

    $k=17;
    $k %= 8;
    echo $k; // 输出 1
?>
```



##### 字符串运算符

| 运算符 | 名称     | 例子                                        | 显示结果                                                     |
| :----- | :------- | :------------------------------------------ | :----------------------------------------------------------- |
| .      | 串接     | \$txt1 = "Hello" \$txt2 = $txt1 . " world!" | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_string1) |
| .=     | 串接赋值 | \$txt1 = "Hello" $txt1 .= " world!"         | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_string2) |

```php
<?php
    $a = "Hello";
    $b = $a . " world!";
    echo $b; // 输出 Hello world!

    $x="Hello";
    $x .= " world!";
    echo $x; // 输出 Hello world!
?>
```

##### 递增/递减运算符

| 运算符 | 名称                          | 显示结果                                                     |
| :----- | :---------------------------- | :----------------------------------------------------------- |
| ++$x   | 前递增,，$x的值加一，然后返回 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_pre_increment) |
| $x++   | 后递增，返回$x的值，然后加一  | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_post_increment) |
| --$x   | 前递减， $x的值减一，然后返回 | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_pre_decrement) |
| $x--   | 后递减，返回$x的值，然后减一  | [显示结果](https://www.w3school.com.cn/tiy/s.asp?f=demo_php_operator_post_decrement) |

```PHP
<?php
    $x=17; 
    echo ++$x; // 输出 18

    $y=17; 
    echo $y++; // 输出 17

    $z=17;
    echo --$z; // 输出 16

    $i=17;
    echo $i--; // 输出 17
?>
```

##### 比较运算符

PHP 比较运算符用于比较两个值（数字或字符串）：

| 运算符 |                  名称                   |    例子    |
| :----: | :-------------------------------------: | :--------: |
|   ==   |        如果类型转换后 $a 等于 $b        | \$x == $y  |
|  ===   | 如果 $a 等于 $b，并且它们的类型也相同。 | \$x === $y |
|   !=   |       如果类型转换后 $a 不等于 $b       | \$x != $y  |
|   <>   |       如果类型转换后 $a 不等于 $b       | \$x <> $y  |
|  !==   |  如果 $a 不等于 $b，或者它们的类型不同  | \$x !== $y |
|   >    |           如果 $a 严格大于 $b           |  \$x > $y  |
|   <    |           如果 $a 严格小于 $b           |  \$x < $y  |
|   >=   |         如果 $a 小于或者等于 $b         | \$x >= $y  |
|   <=   |         如果 $a 大于或者等于 $b         | \$x <= $y  |

```php
<?php
    $x=17; 
    $y="17";

    var_dump($x == $y);
    echo "<br>";
    var_dump($x === $y);
    echo "<br>";
    var_dump($x != $y);
    echo "<br>";
    var_dump($x !== $y);
    echo "<br>";

    $a=17;
    $b=8;

    var_dump($a > $b);
    echo "<br>";
    var_dump($a < $b);
?>
```

##### 逻辑运算符

| 运算符 | 名称 | 例子        | 结果                                              |
| :----- | :--- | :---------- | :------------------------------------------------ |
| and    | 与   | \$x and $y  | 如果 \$x 和 $y 都为 true，则返回 true。           |
| or     | 或   | \$x or $y   | 如果 \$x 和 $y 至少有一个为 true，则返回 true。   |
| xor    | 异或 | \$x xor $y  | 如果 \$x 和 $y 有且仅有一个为 true，则返回 true。 |
| &&     | 与   | \$x && $y   | 如果 \$x 和 $y 都为 true，则返回 true。           |
| \|\|   | 或   | \$x \|\| $y | 如果 \$x 和 $y 至少有一个为 true，则返回 true。   |
| !      | 非   | !$x         | 如果 $x 不为 true，则返回 true。                  |

##### 数组运算符

PHP 数组运算符用于比较数组：

| 运算符 | 名称   | 例子       | 结果                                                         |
| :----- | :----- | :--------- | :----------------------------------------------------------- |
| +      | 联合   | \$x + $y   | \$x 和 $y 的联合（但不覆盖重复的键）                         |
| ==     | 相等   | \$x == $y  | 如果 \$x 和 $y 拥有相同的键/值对，则返回 true。              |
| ===    | 全等   | \$x === $y | 如果 \$x 和 $y 拥有相同的键/值对，且顺序相同类型相同，则返回 true。 |
| !=     | 不相等 | \$x != $y  | 如果 \$x 不等于 $y，则返回 true。                            |
| <>     | 不相等 | \$x <> $y  | 如果 \$x 不等于 $y，则返回 true。                            |
| !==    | 不全等 | \$x !== $y | 如果 \$x 与 $y 完全不同，则返回 true。                       |

```php
<?php
    $x = array("a" => "apple", "b" => "banana"); 
    $y = array("c" => "orange", "d" => "peach"); 
    $z = $x + $y; // $x 与 $y 的联合
    var_dump($z);
    var_dump($x == $y);
    var_dump($x === $y);
    var_dump($x != $y);
    var_dump($x <> $y);
    var_dump($x !== $y);
?>
```



#### if判断

在您编写代码时，经常会希望为不同的决定执行不同的动作。您可以在代码中使用条件语句来实现这一点。

在 PHP 中，我们可以使用以下条件语句：

- *if 语句* - 如果指定条件为真，则执行代码
- *if...else 语句* - 如果条件为 true，则执行代码；如果条件为 false，则执行另一端代码
- *if...elseif....else 语句* - 根据两个以上的条件执行不同的代码块

if 语句用于*在指定条件为 true 时*执行代码。

```php
if (条件) {
  当条件为 true 时执行的代码;
}

<?php
    $t=date("H");

    if ($t<"20") {
      echo "Have a good day!";
    }
?>
```

 if....else 语句在条件为 true 时执行代码，在条件为 false 时执行另一段代码。、

```php
if (条件) {
  条件为 true 时执行的代码;
} else {
  条件为 false 时执行的代码;
}

<?php
    $t=date("H");

    if ($t<"20") {
      echo "Have a good day!";
    } else {
      echo "Have a good night!";
    }
?>
```

if....elseif...else 语句来根据两个以上的条件执行不同的代码

```php
if (条件) {
  条件为 true 时执行的代码;
} elseif (condition) {
  条件为 true 时执行的代码;
} else {
  条件为 false 时执行的代码;
}


<?php
    $t=date("H");

    if ($t<"10") {
      echo "Have a good morning!";
    } elseif ($t<"20") {
      echo "Have a good day!";
    } else {
      echo "Have a good night!";
    }
?>
```



#### switch判断

如果您希望有选择地执行若干代码块之一，请使用 Switch 语句。

使用 Switch 语句可以避免冗长的 if..elseif..else 代码块。

```
switch (expression) {
    case label1:
      expression = label1 时执行的代码 ;
      break;  
    case label2:
      expression = label2 时执行的代码 ;
      break;
    default:
      表达式的值不等于 label1 及 label2 时执行的代码;
}
```

工作原理：

1. 对表达式（通常是变量）进行一次计算
2. 把表达式的值与结构中 case 的值进行比较
3. 如果存在匹配，则执行与 case 关联的代码
4. 代码执行后，*break 语句*阻止代码跳入下一个 case 中继续执行
5. 如果没有 case 为真，则使用 default 语句

```php
<?php
$favfruit="orange";

switch ($favfruit) {
   case "apple":
     echo "Your favorite fruit is apple!";
     break;
   case "banana":
     echo "Your favorite fruit is banana!";
     break;
   case "orange":
     echo "Your favorite fruit is orange!";
     break;
   default:
     echo "Your favorite fruit is neither apple, banana, or orange!";
}
?>
```



#### while循环

在您编写代码时，经常需要反复运行同一代码块。我们可以使用循环来执行这样的任务，而不是在脚本中添加若干几乎相等的代码行。

在 PHP 中，我们有以下循环语句：

- while - 只要指定条件为真，则循环代码块
- do...while - 先执行一次代码块，然后只要指定条件为真则重复循环
- for - 循环代码块指定次数
- foreach - 遍历数组中的每个元素并循环代码块

while循环，只要指定的条件为真，while 循环就会执行代码块。

```php
while (条件为真) {
  要执行的代码;
}

<?php 
	$x=1; 

    while($x<=5) {
      echo "这个数字是：$x <br>";
      $x++;
    } 
?>
```

do...while 循环首先会执行一次代码块，然后检查条件，如果指定条件为真，则重复循环。

```php
do {
  要执行的代码;
} while (条件为真);

<?php 
    $x=1; 

    do {
      echo "这个数字是：$x <br>";
      $x++;
    } while ($x<=5);
?>
```



#### for循环

如果您已经提前确定脚本运行的次数，可以使用 for 循环。

```php
for (init counter; test counter; increment counter) {
  code to be executed;
}
```

参数：

- init counter：初始化循环计数器的值
- test counter： 评估每个循环迭代。如果值为 TRUE，继续循环。如果它的值为 FALSE，循环结束。
- increment counter：增加循环计数器的值

```PHP
<?php 
    for ($x=0; $x<=10; $x++) {
      echo "数字是：$x <br>";
    } 
?>
```

foreach 循环只适用于数组，并用于遍历数组中的每个键/值对。

每进行一次循环迭代，当前数组元素的值就会被赋值给 $value 变量，并且数组指针会逐一地移动，直到到达最后一个数组元素。

```php
foreach ($array as $value) {
  code to be executed;
}

<?php 
    $colors = array("red","green","blue","yellow"); 

    foreach ($colors as $value) {
      echo "$value <br>";
    }
?>
```



#### 函数



##### 无参函数

函数是可以在程序中重复使用的语句块。

页面加载时函数不会立即执行。

函数只有在被调用时才会执行。

用户定义的函数声明以单词 "function" 开头：

```php
function functionName() {
  被执行的代码;
}
```

命名规范：

- 函数名能够以字母或下划线开头（而非数字）。

- 函数名对大小写不敏感。

- 函数名应该能够反映函数所执行的任务。

```php
<?php
    function sayHi() {
      echo "Hello world!";
    }

	sayhi(); // 调用函数
?>
```

##### 有参函数

可以通过参数向函数传递信息。参数类似变量。

参数被定义在函数名之后，括号内部。您可以添加任意多参数，只要用逗号隔开即可。

```php
<?php
function familyName($fname) {
  echo "$fname Zhang.<br>";
}

familyName("Li");
familyName("Hong");
familyName("Tao");
familyName("Xiao Mei");
familyName("Jian");
?>
```



##### 默认参数

在接收参数时候，可以给参数指定一个默认值，当用户没有传递该参数的时候，就使用默认值

```PHP
<?php
    function setHeight($minheight=50) {
      echo "The height is : $minheight <br>";
    }

    setHeight(350);
    setHeight(); // 将使用默认值 50
    setHeight(135);
    setHeight(80);
?>
```



##### 函数返回值

如需使函数返回值，请使用 return 语句

```php
<?php
function sum($x,$y) {
  $z=$x+$y;
  return $z;
}

echo "5 + 10 = " . sum(5,10) . "<br>";
echo "7 + 13 = " . sum(7,13) . "<br>";
echo "2 + 4 = " . sum(2,4);
?>
```



### PHP数组

​	数组能够在单独的变量名中存储一个或多个值。



#### 数组的类型

- *索引数组* - 带有数字索引的数组
- *关联数组* - 带有指定键的数组
- *多维数组* - 包含一个或多个数组的数组



#### 数组的创建

在 PHP 中， array() 函数用于创建数组

可以用短数组语法 `[]` 替代 `array()` 。

也可以接受任意数量用逗号分隔的 `键（key） => 值（value）` 对。

```php
<?php
$array = array(
    "foo" => "bar",
    "bar" => "foo",
);

// 使用短数组语法
$array = [
    "foo" => "bar",
    "bar" => "foo",
];
?>
    
// 数组可以嵌套
<?php
$array = array(
    "foo" => "bar",
    42    => 24,
    "multi" => array(
         "dimensional" => array(
             "array" => "foo"
         )
    )
);

var_dump($array["foo"]);
var_dump($array[42]);
var_dump($array["multi"]["dimensional"]["array"]);
?>
    
// 值的添加，修改，删除
<?php
$arr = array(5 => 1, 12 => 2);

$arr[] = 56;    // 这与 $arr[13] = 56 相同;
                // 在脚本的这一点上

$arr["x"] = 42; // 添加一个新元素
                // 键名使用 "x"
                
unset($arr[5]); // 从数组中删除元素

unset($arr);    // 删除整个数组
?>
```



#### PHP 索引数组

有两种创建索引数组的方法：

索引是自动分配的（索引从 0 开始）：

```
$cars=array("porsche","BMW","Volvo");
```

或者也可以手动分配索引：

```
$cars[0]="porsche";
$cars[1]="BMW";
$cars[2]="Volvo";
```

下面的例子创建名为 $cars 的索引数组，为其分配三个元素，然后输出包含数组值的一段文本：

```
<?php
$cars=array("porsche","BMW","Volvo");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
?>
```



**获取数组的长度**

​	count() 函数用于返回数组的长度（元素数）

```php
<?php
    $cars=array("porsche","BMW","Volvo");
    echo count($cars);
?>
```



**索引数组的遍历**

如需遍历并输出索引数组的所有值，您可以使用 for 循环，就像这样：

```php
<?php
$cars=array("porsche","BMW","Volvo");
$arrlength=count($cars);

for($x=0;$x<$arrlength;$x++) {
  echo $cars[$x];
  echo "<br>";
}
?>
```



#### PHP 关联数组

关联数组是使用您分配给数组的指定键的数组。

有两种创建关联数组的方法：

```php
$age=array("Bill"=>"35","Steve"=>"37","Elon"=>"43");
```

或者：

```php
$age['Bill']="63";
$age['Steve']="56";
$age['Elon']="47";
```

随后可以在脚本中使用指定键：

```php
<?php
    $age=array("Bill"=>"63","Steve"=>"56","Elon"=>"47");
    echo "Elon is " . $age['Elon'] . " years old.";
?>
```

**遍历关联数组**

​	如需遍历并输出关联数组的所有值，您可以使用 foreach 循环，就像这样

```php
<?php
    $age=array("Bill"=>"63","Steve"=>"56","Elon"=>"47");

    foreach($age as $x=>$x_value) {
      echo "Key=" . $x . ", Value=" . $x_value;
      echo "<br>";
    }
?>
```



#### PHP - 多维数组

多维数组指的是包含一个或多个数组的数组。

PHP 能理解两、三、四或五级甚至更多级的多维数组。不过，超过三级深的数组对于大多数人难于管理。

**注意：**数组的维度指示您需要选择元素的索引数。

- 对于二维数组，您需要两个索引来选取元素
- 对于三维数组，您需要三个索引来选取元素



**PHP二维数组**

两维数组是数组的数组（三维数组是数组的数组的数组）。

```php
<?php
$cars = array
  (
  array("Volvo",22,18),
  array("BMW",15,13),
  array("Saab",5,2),
  array("Land Rover",17,15)
  );
    
    echo $cars[0][0].": 库存：".$cars[0][1].", 销量：".$cars[0][2].".<br>";
    echo $cars[1][0].": 库存：".$cars[1][1].", 销量：".$cars[1][2].".<br>";
    echo $cars[2][0].": 库存：".$cars[2][1].", 销量：".$cars[2][2].".<br>";
    echo $cars[3][0].": 库存：".$cars[3][1].", 销量：".$cars[3][2].".<br>";
?>
```

我们也可以在 For 循环中使用另一个 For 循环，来获得 $cars 数组中的元素（我们需使用两个索引）：

```php
<?php
    for ($row = 0; $row < 4; $row++) {
      echo "<p><b>Row number $row</b></p>";
      echo "<ul>";
      for ($col = 0; $col < 3; $col++) {
        echo "<li>".$cars[$row][$col]."</li>";
      }
      echo "</ul>";
    }
?>

```

#### PHP数组的排序函数

- sort() - 以升序对数组排序

```php
<?php
    $cars=array("porsche","BMW","Volvo");
    sort($cars);

	$numbers=array(3,5,1,22,11);
	sort($numbers);
?>
```

- rsort() - 以降序对数组排序

```php
<?php
    $cars=array("porsche","BMW","Volvo");
    rsort($cars);
	$numbers=array(3,5,1,22,11);
	rsort($numbers);
?>
```

- asort() - 根据值，以升序对关联数组进行排序

```php
<?php
    $age=array("Bill"=>"63","Steve"=>"56","Elon"=>"47");
    asort($age);
?>
```

- ksort() - 根据键，以升序对关联数组进行排序

```php
<?php
    $age=array("Bill"=>"63","Steve"=>"56","Elon"=>"47");
    ksort($age);
?>
```

- arsort() - 根据值，以降序对关联数组进行排序

```php
<?php
    $age=array("Bill"=>"63","Steve"=>"56","Elon"=>"47");
    arsort($age);
?>
```

- krsort() - 根据键，以降序对关联数组进行排序

```php
<?php
    $age=array("Bill"=>"63","Steve"=>"56","Elon"=>"47");
    krsort($age);
?>
```



#### PHP超全局变量

PHP 中的许多预定义变量都是“超全局的”，这意味着它们在一个脚本的全部作用域中都可用。在函数或方法中无需执行 global $variable; 就可以访问它们。

这些超全局变量是：

- $GLOBALS
- $_SERVER
- $_REQUEST
- $_POST
- $_GET
- $_FILES
- $_ENV
- $_COOKIE
- $_SESSION

本节会介绍一些超全局变量，并会在稍后的章节讲解其他的超全局变量。



**$GLOBALS — 引用全局作用域中可用的全部变量**

$GLOBALS 这种全局变量用于在 PHP 脚本中的任意位置访问全局变量（从函数或方法中均可）。

PHP 在名为 $GLOBALS[index] 的数组中存储了所有全局变量。变量的名字就是数组的键。



**PHP $_SERVER**

$_SERVER 这种超全局变量保存关于报头、路径和脚本位置的信息。



**PHP $_REQUEST**

用于收集 HTML 表单提交的数据。



**PHP \$_POST**

广泛用于收集提交 method="post" 的 HTML 表单后的表单数据。$_POST 也常用于传递变量。



**PHP $_GET** 

用于收集提交 HTML 表单 (method="get") 之后的表单数据。