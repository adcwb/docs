https://mp.weixin.qq.com/s/vwGlL7xNXszTr6mEKLXtZA

## BIND DNS使用

### 1、安装

```bash
# Centos安装
	yum -y install bind 

# 查看需要修改的配置文件所在路径


	rpm -qc bind                   # 查询bind软件配置文件所在路径
	/etc/named.conf                # 主配置文件
	/etc/named/rfc1912.zonrs       # 区域配置文件
	/var/named/named.localhost     # 区域数据配置文件
```

### 2、配置

编辑主配置文件named.conf

```BASH
# vim /etc/named.conf
options {
  listen-on-v6 poet 53 { 192.168.184.10; };              #监听53端口，IP地址使用提供服务的本地IP，也可用any代表所有
# listen-on-v6 port 53 { : :1; };                      #ipv6行如不使用可以注释掉或者删除
  directory       "/var/named";                          #区域数据文件的默认存放位 置
  dump- file      "/var/ named/data/cache_ dump . db";   #域名缓存数据库文件的位置
  statistics-file "/var/named/data/named stats.txt";     #状态统计文件的位置
  memstatistics-file "/var/named/data/named_ mem_ stats. txt";    #内存统计文件的位置
  allow-query       { any; };                            #允许使用本DNS解析服务的网段，也可用any代表所有

```

编辑区域配置文件

```bash
im /etc/named. rfc1912. zone               #文件里有模版，可复制粘贴后修改
zone "80.168.192. in-addr.arpa" IN {        #反向解析的地址倒过来写，代表解析192.168.80段的地址
         type master;
         file "benet. com. zone. local";    #指定区域数据文件为benet.com.zone.local
         allow-update { none; } ;
```

