### Django基础

​	列表元素删除问题

```python
在遍历列表的时候，因为删除元素后，整个列表的元素的索引会移动，提供以下几种方法，仅供参考

解决方法：
	1.遍历在新的列表操作，删除是在原来的列表操作
        a = [1,2,3,4,5,6,7,8]
        print(id(a)) 
        print(id(a[:])) 
        for i in a[:]:
            if i>5:
                pass
            else:
                a.remove(i)
            print(a)
        print('-------------------------')
        print(id(a))

	2.使用filter内建函数
    	a = [1,2,3,4,5,6,7,8]
        b = filter(lambda x: x>5,a)
        print(b)

	3.列表解析
    	a = [1,2,3,4,5,6,7,8]
        b = [i for i in a if i >5]
        print(b)
       
    4.倒序删除
    	因为列表总是“向前移”，所以可以倒序遍历，即使后面的元素被修改了，还没有被遍历的元素和其坐标还是保持不变的
        a = [1,2,3,4,5,6,7,8]
        print(id(a))
        for i in range(len(a)-1,-1,-1):
            if a[i] > 5:
                pass
            else:
                a.remove(a[i])
        print(id(a))
        print('-------------------------')
        print(a)
     
```



### Django数据库操作

#### Django操作MySQL

```python
Django默认用的数据库是sqlite3
在setting.py中找到关于SQL的配置项：
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

若要改为MySQL数据库，要先在配置文件中配置
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_base',
            'USER': 'root',
            'PASSWORD': 'your_password',
            'HOST': '118.25.65.95',
            'PORT': '3306',
            'CHARSET': 'UTF8'
        }
    }
配置完成后，需要做一个声明：
	django默认用的是mysqldb模块链接MySQL，但是该模块的兼容性不好，需要手动改为用pymysql连接
    需要告诉django不要用默认的mysqldb 而是用pymysql
	在项目名下的init或者任意的应用名下的init文件中书写以下代码都可以
    	import pymysql
		pymysql.install_as_MySQLdb()
```



若想要在每个app中使用单独的数据库，可以使用一下方法

```Python
app配置单独的数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
        'USER':'root',　　　　　　  # 连接数据库的用户名
        'PASSWORD':'',　　　　　　  # 连接数据库的密码
        'HOST':'127.0.0.1',       # 连接主机，默认本级
        'PORT'：3306    　　　     #  端口 默认3306
    }，
    
    'app01': { #可以为每个app都配置自己的数据，并且数据库还可以指定别的，也就是不一定就是mysql，也可以指定sqlite等其他的数据库
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'bms',     　　 　  # 要连接的数据库，连接前需要创建好
        'USER':'root',　　　　　　  # 连接数据库的用户名
        'PASSWORD':'',　　　　　　  # 连接数据库的密码
        'HOST':'127.0.0.1',       # 连接主机，默认本级
        'PORT'：3306    　　　     #  端口 默认3306
    }
}

```



#### Django操作SQL Server

​	Django框架默认是不支持连接sql server数据库的，需要先安装驱动，然后才可以使用

```python
安装如下驱动：
	pip3 install django-pyodbc django-pyodbc-azure django-pytds pyodbc  pywin32 django-mssql django-sqlserver
 
修改Django的配置文件：
	DATABASES = {
    # sql server
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'ceshi',
        'HOST': '103.60.220.44',
        'PORT': '49334',
        'USER': 'whao',
        'PASSWORD': 'KF-idc.wanghao',
        'OPTIONS': {
            'driver': 'ODBC Driver 11 for SQL Server',
            'MARS_Connection': True,
        },
    }
}
    
注意：
    若出现以下错误
    	django.db.utils.InterfaceError: ('IM002', '[IM002] [Microsoft][ODBC 驱动程序管理器] 未发现数据源名称并且未指定默认驱动程序 (0) (SQLDriverConnect)')
    
    在Windows开发环境下，需要先确定是否本地有相对应driver，直接在搜索框搜索ODBC数据源，然后点击驱动程序查看即可，若没有相应的驱动，需要先安装驱动
    
    在Linux生产环境中，默认是没有ODBC Driver 11 for SQL Server驱动的，可以改为SQL Server Native Client 11.0，同时需要安装sqlncli驱动，才可以使用，建议在Linux系统中，以编译安装的方式部署Python开发环境
    
```



在CentOS 7系统中编译安装Python3

```bash
一、安装依赖包
	yum install zlib-devel bzip2-devel openssl* ncurses-devel sqlite-devel readline-devel tk-devel gcc* make wget net-tools vim unzip
	yum -y install unixODBC* 
	yum install libtool-ltdl libtool-ltdl-devel
	wget http://download.microsoft.com/download/6/A/B/6AB27E13-46AE-4CE9-AFFD-406367CADC1D/Linux6/sqlncli-11.0.1790.0.tar.gz
	tar xvf sqlncli-11.0.1790.0.tar.gz
    cd sqlncli-11.0.1790.0
    ./install.sh verify
    ldd lib64/libsqlncli*
    ./install.sh install --force
    
    vim /etc/odbcinst.ini
    	[SQL Server Native Client 11.0]
        Description=Microsoft SQL Server ODBC Driver V1.0 for Linux
        Driver=/opt/microsoft/sqlncli/lib64/libsqlncli-11.0.so.1790.0
        Threading=1
        UsageCount=1
    

	
	编译安装python3
		wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
		wget http://download.microsoft.com/download/6/A/B/6AB27E13-46AE-4CE9-AFFD-406367CADC1D/Linux6/sqlncli-11.0.1790.0.tar.gz
		tar -zxvf  Python-3.6.8.tgz			# 解压
		cd Python-3.6.8
		./configure --prefix=/usr/local/python3　&& make && make install
		
	安装虚拟环境
		pip3 install virtualenv
		pip3 install virtualenvwrapper
		mkdir $HOME/.virtualenvs
		vim .bashrc
			export WORKON_HOME=$HOME/.virtualenvs
			export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3/bin/python3
		source /usr/local/python3/bin/virtualenvwrapper.sh

		
	pip导出本地已安装的Python模块
		pip freeze > requirements.txt
		
	从导出的文件中安装模块
		pip install -r quirements.txt

```



#### Django操作Redis

```python
安装：
	pip install django-redis
  
作为 cache backend 使用配置：
	CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
    
    支持三种 URL scheme :
        redis://: 普通的 TCP 套接字连接
        rediss://: SSL 包裹的 TCP 套接字连接
        unix://: Unix 域套接字连接
        redis://[:password]@localhost:6379/0
        rediss://[:password]@localhost:6379/0
        unix://[:password]@/path/to/socket.sock?db=0
           
作为 session backend 使用配置
	Django 默认可以使用任何 cache backend 作为 session backend, 将 django-redis 作为 session 储存后端不用安装任何额外的 backend
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


参考文档：
	https://django-redis-chs.readthedocs.io/zh_CN/latest/
```



#### Django操作MongoDB

​	Python中有关MongoDB的操作都需要依赖于pymongo模块

```python
安装：	
	pip install pymongo

数据库连接(无密码)：
	import pymongo
	mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
   
数据库连接(有密码)：

	# 方式1：
    import pymongo
    from urllib import parse
    username = parse.quote_plus('django')   # 对用户名进行编码
    password = parse.quote_plus('123456')  # 对密码进行编码
    database = "django" # 数据库名称
    host     = "127.0.0.1"
    port     = "27017"
    mongo = pymongo.MongoClient('mongodb://%s:%s@%s:%s/%s' % ( username, password, host, port, database))


    # 方式2：
    import pymongo
    from urllib import parse
    username = parse.quote_plus('django')   # 对用户名进行编码
    password = parse.quote_plus('123456')  # 对密码进行编码
    database = "django" # 数据库名称
    mongo = pymongo.MongoClient('mongodb://127.0.0.1:27017') # 组装成url进行连接
    my_db = mongo["django"]
    my_db.authenticate(username,password)

    # 方式3：
    import pymongo
    from urllib import parse
    username = parse.quote_plus('root')   # 对用户名进行编码
    password = parse.quote_plus('123456')  # 对密码进行编码
    host     = "127.0.0.1"
    port     = "27017"
    database = "django" # 数据库名称
    mongo = pymongo.MongoClient('mongodb://%s:%s@%s:%s/admin' % ( username, password, host, port))
    my_db = mongo[database]
    my_collection = my_db["my_collection"] # 没有往集合里面保存文档之前，mongdb不会真正创建集合!

```



### Django自定义jwt

```python
项目地址：
	https://github.com/jpadilla/django-rest-framework-jwt

背景：
	from django.urls import path
    from rest_framework_jwt.views import obtain_jwt_token
    urlpatterns = [
        path('login/', obtain_jwt_token),
    ]

    path('login/', obtain_jwt_token)其实相当于path('login/', ObtainJSONWebToken.as_view())
    因为我们之间进源码可以看到
        obtain_jwt_token = ObtainJSONWebToken.as_view()     #获得
        refresh_jwt_token = RefreshJSONWebToken.as_view()   #刷新
        verify_jwt_token = VerifyJSONWebToken.as_view()     #验证
        
	但是要想使用obtain_jwt_token，就必须要使用Django标准的User模型类（一般都是继承django.contrib.auth.models.AbstractUser），但是在生产环境中，不太可能每次项目表都是重新设计的，往往很多时候都是使用的已经存在的表，因此需要想一个办法既能实现自动认证鉴权，又能灵活切换表
    
    
分析：
	登录就是通过校验用户名和密码，验证通返回token，目前只能考虑在加密环节动手脚
    通过分析可知，jwt加密环节有现成的函数jwt_encode_handler(payload)可用
    payload参数的实质就是一个字典，，jwt组件是使用user示实例生成的，现在需要想办法使用需求中的表生成，且要确保这个字典中包含唯一标识一条表记录的字段，比如用户的id，还要包含token的过期时间等，然后传入jwt_encode_handler进行加密，最后返回前端
    jwt_decode_handler应使用相反的流程去解析token，然后提取信息去需求表中查找记录并验证信息是否正确，token时间是否过期，若没问题则通过认证，但是要注意，默认走的还是user表，需要想办法换成自己的表
    续签token
    
    
    

实现：
	
```



​		

### Django自定义auth

```python

```





### Django ORM外键关系

```

 外界开发中，不过是SQLAlachemy或者django的ORM，大部分的公司都会放弃使用外键约束来关联查询数据库表。
 因为外键约束，在数据库操作过程中，需要消耗额外的维护成本来管理这个外键关系。因此在大数据的查询中，一般都会设置成逻辑外键[虚拟外键]。数据库本身维护的外键一般我们称之为 "物理外键".
 django的ORM中，要设置虚拟外键：外键字段中设置 db_constraint=False
 	字段名 = models.ForeignKey(关联模型, db_constraint=False)
 SQLAlachemy中，要设置虚拟外键，https://graycarl.me/2016/12/27/sqlalchemy-without-foreignkey.html
    # 一对一/多对一
 	字段名 = db.relationship(
        '关联模型',
        primaryjoin='主模型.id == 关联模型.parent_id',
        foreign_keys='关联模型.parent_id',
        uselist=False,
        backref='反向调用的字段别名')
        
    # 多对多/一对多
    字段名 = db.relationship(
        "关联模型",
        secondary=association_table,
        primaryjoin='左表.id == 关系表.left_id',
        secondaryjoin='右表.id == 关系表.right_id',
        uselist=True,
        backref='反向调用的字段别名')




```

