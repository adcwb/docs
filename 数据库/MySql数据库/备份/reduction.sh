#!/bin/bash

db_user="root"
db_passwd="V3QM\$FhKuSqcP@Xk<H+U8wIC_m1T?vn>"
read -p "请输入要恢复的日期: " date
#bk_file=`find /backup/ -name mysqlbk_$date*.gz`
bk_file=/backup/mysqlbk-$date.tar.gz

systemctl stop mysqld
if [ $? -eq 0 ]; then
    rm -rf /var/lib/mysql/*
    tar -zxf $bk_file -C /var/lib/mysql/ >& ./reduction.log
    mv /var/lib/mysql/backup/$date/* /var/lib/mysql/ && rm -rf /var/lib/mysql/backup
    if [ $? -eq 0 ]; then
        echo "tar file Success~"
    else
        echo "tar file Error!!!"
    fi
else
    echo "stop mysql error"
fi

innobackupex  --user=$db_user  --password=$db_passwd  --apply-log /var/lib/mysql  >& ./reduction.log

if [ $? -eq 0 ]; then
    chown -R mysql:mysql /var/lib/mysql
    systemctl restart mysqld
    if [ $? -eq 0 ]; then
        echo "mysql start Success~"
        echo "mysql reduction Success~"
    else
        echo "start mysql error"
    fi
else
    echo "reduction Error"
fi
