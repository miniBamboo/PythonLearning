# -*- coding:utf-8 -*-
import socket
sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.sendall(bytes("欢迎光临文件传输系统",encoding="utf-8"))

    size = conn.recv(1024)
    size_str = str(size, encoding="utf-8")
    print('文件长度:',size_str)
    file_size = int(size_str)
    conn.sendall(bytes("开始传送", encoding="utf-8"))
    has_size = 0
    f = open("hill_new.jpg","wb")
    while True:
        if file_size == has_size:
            break
        date = conn.recv(1024)
        f.write(date)
        has_size += len(date)
    print('文件接收完毕，收到长度:',has_size)
    f.close()


