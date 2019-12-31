#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# socket_server.py


import socket
import deco_http_server


HOST = ''
PORT = 8000
ADDR = (HOST, PORT)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)
sock.listen(1)
print('启动http服务')

while True:
    print('等待连接：')
    conn, addr = sock.accept()
    print('成功连接：', addr)
    data = conn.recv(BUFSIZE)
    if data:
        req_path = data.decode('utf-8').splitlines()[0]
        host = data.decode('utf-8').splitlines()[1]
        # print('收到数据的第一行：', req_path)
        method, path, http = req_path.split()
        print(f'切换URL地址到{host}{path}')
        app = deco_http_server.app
        response = app.call_method(name=path)
        conn.sendall(response)
        conn.close()
