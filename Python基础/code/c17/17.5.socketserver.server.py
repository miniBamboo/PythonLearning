# -*- coding:utf-8 -*-
import  socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes("你好，我是Echo机器人",encoding="utf-8"))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str( ret_bytes, encoding="utf-8")
            if ret_str == "q":
                break
            conn.sendall(bytes("Echo:"+ret_str,encoding="utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1",8080),Myserver)
    server.serve_forever()


