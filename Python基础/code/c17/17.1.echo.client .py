# -*- coding:utf-8 -*-
import socket
ADDR=('127.0.0.1',9999)
#买手机
s=socket.socket()
#拨号
s.connect(ADDR)  #链接服务端，如果服务已经存在一个好的连接，那么挂起
welcom_msg = s.recv(200).decode()#获取服务端欢迎消息
print(welcom_msg)
while True:        #基于connect建立的连接来循环发送消息
    send_data=input("Say:").strip()
    if send_data=='exit':
        s.send(bytes(send_data,encoding='utf8'))
        break
    if len(send_data) == 0:continue
    s.send(bytes(send_data,encoding='utf8'))    
    recv_msg=s.recv(1024)
    print(str(recv_msg,encoding='utf8'))
    #挂电话
s.close()
