#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from  socket import *
import sys
from time import ctime

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
tcpServSock.listen(2)

while True:
	print("waitting for connect...")
	tcpCliSock, addr = tcpServSock.accept()
	print("connect from:", addr)
	
	while True:
		data = tcpCliSock.recv(BUFSIZE)
		if not data:
			break
		print(data.decode('utf-8'))
		data = input('> ')
		tcpCliSock.send(bytes(data, 'utf-8'))
	tcpCliSock.close()
tcpServSock.close()
