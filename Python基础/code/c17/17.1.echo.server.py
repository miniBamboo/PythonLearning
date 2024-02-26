# -*- coding:utf-8 -*-
import socket
ADDR=('127.0.0.1',9999) #定义元祖
#买手机
s=socket.socket()  #绑定协议，生成套接字
s.bind(ADDR) #绑定ip+协议+端口：用来唯一标识一个进程，ip_port必须是元组格式
s.listen(5)        #定义最大可以挂起链接数
#等待电话
while True:  #用来重复接收新的链接
    conn, addrs = s.accept()   #接收客户端的接请求，返回conn（相当于一个特定链接），addrs是客户端(ip,port)
    conn.sendall(bytes('欢迎进入ECHO系统.',encoding='utf-8'))
    #收消息
    while True: #用来基于一个链接重复收发消息
        try: #捕捉客户端异常关闭（ctrl+c）
            recv_data=conn.recv(1024) #收消息，阻塞
            if len(recv_data) == 0:
                break #客户端如果退出，服务端将收到空消息，退出
            recv_str=str(recv_data,encoding='utf8')
            print(addrs[0],'say:',recv_str)
            if recv_str=='exit':
                print(addrs[0],' 退出了')
                break #退出，然后conn.close()关闭客户端            
            #发消息
            send_data=bytes('ECHO:'+recv_str,encoding='utf8')           
            conn.send(send_data) #发送数据            
        except Exception:
            print("异常退出")
            break
    #挂电话
    conn.close()

