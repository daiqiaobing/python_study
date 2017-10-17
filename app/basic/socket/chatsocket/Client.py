# -*- coding: utf-8 -*-
import socket

import time


def client(ip):
    sk = socket.socket()
    sk.connect(ip)
    time.sleep(4)
    msg = {'status': True, 'leave': True, 'msg': '我下线了！'}
    sk.sendall(str(msg))
    server_reply = sk.recv(1024)
    print str(server_reply)
    print '我下线了'

if __name__ == '__main__':
    address = ('localhost', 9991)
    client(address)
