# -*- coding: utf-8 -*-
import json
import socket


def service(host, port):
    sk = socket.socket()
    sk.bind((host, port))
    sk.listen(5)
    while True:
        print 'server waiting ..........'
        # 等待链接,阻塞，直到渠道链接 conn打开一个新的对象 专门给当前链接的客户端 addr是ip地址
        con, addr = sk.accept()
        # 获取客户端请求数据
        client_data = con.recv(1024)
        print str(client_data)
        # 向对方发送数据
        con.sendall('不要回答,不要回答,不要回答')
        # con.close()


if __name__ == "__main__":
    HOST, PORT = 'localhost', 9991
    service(HOST, PORT)
