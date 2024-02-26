# -*- coding:utf-8 -*-
import socket
import os

obj = socket.socket()
obj.connect(("127.0.0.1",8080))
ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8")
print(ret_str)

size = os.stat("hill.jpg").st_size
print('待发送文件长度:',size)
obj.sendall(bytes(str(size),encoding="utf-8"))

obj.recv(1024)

with open("hill.jpg","rb") as f:
    for line in f:
        obj.sendall(line)

print('文件发送完毕。')
