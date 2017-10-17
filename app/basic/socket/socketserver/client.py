# -*- coding: utf-8 -*-
import socket
import sys


def client():
    HOST, PORT = "localhost", 9999
    data = "mango "

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(data)

        # Receive data from the server and shut down
        received = str(sock.recv(1024))
        print received
    finally:
        sock.close()

if __name__ == '__main__':
    client()
