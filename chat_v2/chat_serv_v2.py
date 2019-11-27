#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from  socket import *
import threading
import sys


if len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
else:
    HOST = 'localhost'
    PORT = 8964

ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

print("waitting for connect...")
tcpCliSock, addr = tcpServSock.accept()
print("connect from:", addr)


def receive(tcpCliSock):
    while True:
        data = tcpCliSock.recv(BUFSIZE).decode('utf-8')
        if data == 'quit':
            break
        print("message from %s:%s" %(addr, data))


thrd = threading.Thread(target=receive, args=(tcpCliSock,))
thrd.start()

while True:
    data = input('serv> ')
    if data == 'quit':
        break
    tcpCliSock.send(bytes(data, 'utf-8'))

tcpServSock.close()
