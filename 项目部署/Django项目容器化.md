- Django工程容器化简介
		由于在开发中难免会经常测试一些项目，但是每次都需要重新安装环境，特别不方便，若使用容器化技术的，开箱即用，大大节约了时间成本

- 镜像说明
		基础镜像为`adcwb/images:python3.6.8`，已上传DockerHub，压缩后的镜像大小为355M
		基础镜像为自封装的centos7镜像
		在镜像中安装了一些基本的编译环境，然后编译安装Python3
		在镜像中安装sqlncli数据库驱动程序
		该镜像已经内置了sql server数据库驱动，Nginx应用及一些基本的管理命令
		基础镜像详细封装步骤如下所示

- Docker安装
```
	1、安装需要的软件包， yum-util 提供yum-config-manager功能，另两个是devicemapper驱动依赖
		yum install -y yum-utils device-mapper-persistent-data lvm2
		
	2、配置yum源，任选一个即可，国内建议使用阿里源
		yum-config-manager --add-repo http://download.docker.com/linux/centos/docker-ce.repo（官方源）
		yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo（阿里源）

	3、安装docker
		yum list docker-ce --showduplicates | sort -r	# 列出所有可用版本
		yum -y install docker-ce

	4、启动docker
		systemctl start docker		# 启动
		systemctl restart docker	# 重启
		systemctl stop docker		# 停止
		systemctl status docker		# 查看当前docker状态
		systemctl enable docker		# 开机启动
		systemctl disable docker	# 禁止开机启动
```


- DockerFile文件-Django通用

```
├── config						# 配置文件存放目录
│   └── requirements.txt		# Django项目依赖包
├── docker-compose.yml
├── Dockerfile					# 制作镜像的步骤
└── project						# 项目存放的位置
    └── uwsgi.ini				# uwsgi配置文件所在路径

```
```
		FROM adcwb/images:python3.6.8
		ENV PYTHONUNBUFFERED 1

		RUN mkdir /root/config && mkdir /root/src
		ADD config/requirements.txt /root/config/
		ADD project/ /root/src
		RUN pip3 install -r /root/config/requirements.txt
		RUN /usr/local/python3/bin/uwsgi --ini /root/src/uwsgi.ini
```

- Docker常用命令
```
	删除所有退出的镜像
		docker rm `docker ps -a | grep Exited | awk '{print $1}'`
	
	删除名称或者标签为空的镜像
		docker rmi -f  `docker images | grep '<none>' | awk '{print $3}'`
		docker images|grep none|awk '{print $3}'|xargs docker rmi
```

- Cnetos7编译安装Python3.6

```
	1、安装基本的编译环境
		yum -y groupinstall "Development tools"
		yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

	2、下载安装包并解压
		wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
		# 解压包
		tar -xvf Python-3.6.8.tar.xz

	3、编译安装Python
		# 进入解压目录
			cd Python-3.6.8

		# 生成MakeFile
			./configure --prefix=/usr/local/python3.6.8 --enable-optimizations

		# 安装 使用make atinstall避免替换默认的python执行文件
			Make && make altinstall

	4、设置软连接，更新pip
		ln -s /usr/local/python3.6.8/bin/python3.6 /usr/bin/python3
		ln -s /usr/local/python3.6.8/bin/pip3.6 /usr/bin/pip3
		pip3 install --upgrade pip setuptools

	5、更改pip默认源
		mkdir ~/.pip
		cd ~/.pip
		vim pip.conf

		写入下面代码，将pip源设置为阿里源
			[global]
			index-url=http://mirrors.aliyun.com/pypi/simple/

			[install]
			trusted-host=mirrors.aliyun.com

	6、安装虚拟环境
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

- Centos7编译安装sqlncli数据库驱动程序
```
	1、从微软官方下载驱动程序包
		wget http://download.microsoft.com/download/6/A/B/6AB27E13-46AE-4CE9-AFFD-406367CADC1D/Linux6/sqlncli-11.0.1790.0.tar.gz

	   安装ODBC驱动
	     yum install libtool-ltdl libtool-ltdl-devel
		 yum -y install unixODBC*

	2、解压并验证安装条件
		tar xvf sqlncli-11.0.1790.0.tar.gz
		cd sqlncli-11.0.1790.0
		./install.sh verify
		验证情况，及依赖关系示例如下，一般前三个选项都是ok的
		若前三个没有显示ok，建议查看是否安装libtool-ltdl libtool-ltdl-devel
```
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/fbf3671f69829dcb61d66327fffa4466)
![](https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/cb7c3e7c50aec98f1e593bf86460f804)

```
	若发现有libodbcinst.so.1 => not found的情况
	可以建立个此缺少环境组件名称的软连接并指向此环境组件的高版本，如：
		cd /usr/lib64
		ln -s libodbcinst.so.2.0.0 libodbcinst.so.1

	完成以后可以再次验证，需要保证验证依赖关系没有问题

	登录数据库测试,当现实>1字符样式的时候就表示登录成功，驱动安装完成
	
		sqlcmd -S 192.168.31.25 -U sa -P '123456'
		> 1

	配置unixOBDC
		vim /etc/odbcinst.ini

		[SQL Server Native Client 11.0]
		Description=Microsoft SQL Server ODBC Driver V1.0 for Linux
		Driver=/opt/microsoft/sqlncli/lib64/libsqlncli-11.0.so.1790.0
		Threading=1
		UsageCount=1
```

