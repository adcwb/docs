#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import struct
import time


def wake_up():
    # 要唤醒主机的mac地址
    MAC = 'DC-4A-3E-78-3E-0A'
    # 要唤醒主机所在的网段的广播地址
    BROADCAST = "192.168.10.255"

    # 判断Mac地址的长度
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")

    mac_address = MAC.replace("-", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''

    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        print("Done")

    except Exception as e:
        print("Error: ", e)


def wark_off():
    # 关机
    os.system('shutdown -s -t 00')


if __name__ == '__main__':
    wake_up()
