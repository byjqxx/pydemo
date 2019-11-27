#!/usr/bin/env python3

from socket import *
import sys
import threading

if len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
else:
    HOST = 'localhost'
    PORT = 8964


ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpCliSock1 = socket(AF_INET, SOCK_STREAM)
tcpCliSock1.connect(ADDR)

def receive(tcpCliSock):
    while True:
        data = tcpCliSock1.recv(BUFSIZE).decode('utf-8')
        if data == 'quit':
            break
        print('message from %s:%s' %(ADDR,data))

thrd = threading.Thread(target=receive, args=(tcpCliSock1,))
thrd.start()

while True:
        data = input('clnt> ')
        if data == 'quit':
            break
        tcpCliSock1.send(bytes(data, 'utf-8'))

tcpCliSock1.close()
