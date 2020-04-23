#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# http_server.py


import json
import socket
from pagecounter import PageCounter
import minitoutiao as mt


HOST = ''  # localhost: 本机，ip值，空：任意主机都可以访问
PORT = 8000
ADDR = (HOST, PORT)
BUFSIZE = 1024

# 新建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP相关参数

# 绑定地址
sock.bind(ADDR)

# 监听连接的个数
sock.listen(1)

print('启动http服务')

# 启动redis
pagecounter = PageCounter()

# 循环发送和接收数据
while True:
    # 等待连接
    print('等待连接：')
    conn, addr = sock.accept()
    print('成功连接：', addr)

    # 循环接收
    data = conn.recv(BUFSIZE)
    # print('收到数据： ', data.decode('utf-8'))  # 处理中文数据的显示
    if data:
        req_path = data.decode('utf-8').splitlines()[0]
        # print('收到数据第一行：', req_path)
        method, path, http = req_path.split()
        print(f'切换URL地址到{path[1:]}')
        path_split = path.split('/')
        dic = {}
        status_404 = "<h1>404 not found</h1>"
        if path_split[1] == 'article' and len(path_split) == 3:
            if path_split[2] == 'all':
                articles = mt.session.query(mt.Article).all()
                data = []
                for article in articles:
                    art_dic = {}
                    author = mt.session.query(mt.Author).filter(
                        mt.Author.id == article.author_id).one()
                    art_dic['id'] = article.id
                    art_dic['author'] = author.name
                    art_dic['title'] = article.title
                    art_dic['content'] = article.content
                    data.append(art_dic)
                dic['status'] = 0
                dic["statusText"] = "所有文章数据"
                dic['articles'] = data
                pagecounter.count_page('articles', 'all')
                count = pagecounter.query_page('articles', 'all')
                print(f'主页的访问量是{count}')
            else:
                try:
                    article_id = int(path_split[2])
                    article = mt.session.query(mt.Article).filter(
                        mt.Article.id == article_id).one()
                    author = mt.session.query(mt.Author).filter(
                        mt.Author.id == article.author_id).one()
                    art_dic = {}
                    art_dic['id'] = article_id
                    art_dic['title'] = article.title
                    art_dic['content'] = article.content
                    dic['author'] = author.name
                    dic['article'] = art_dic
                    pagecounter.count_page(author.name, article.title)
                    count = pagecounter.query_page(author.name, article.title)
                    print(f'{author.name}的{article.title}的访问量是{count}')
                except Exception:
                    dic = status_404
        else:
            dic = status_404

        if dic != status_404:
            json_data = json.dumps(dic)
        else:
            json_data = status_404
        response = f"""HTTP/1.1 200 ok

        {json_data}
        """.encode('gbk')

        conn.sendall(response)  # 在这里处理数据

        conn.close()

sock.close()
