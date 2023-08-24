#!/bin/bash
#mysql自动备份并压缩脚本
#定义环境变量

db_user="root"
db_passwd="V3QM\$FhKuSqcP@Xk<H+U8wIC_m1T?vn>"
bk_time=`date +"%Y-%m-%d"`
#开始备份
innobackupex --user=$db_user --password=$db_passwd --no-timestamp /backup/$bk_time  >& /backup/backup.log
if [ $? -eq 0 ]; then
	tar zcPf /backup/mysqlbk-$bk_time.tar.gz /backup/$bk_time --remove-files
	echo -e "\033[32m`date +%X` backup success\033[0m"
else
	echo -e "\033[31m`date +%X` backup failed\033[0m"
fi
