#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# pagecounter.py


import redis


class PageCounter:

    def __init__(self, host='localhost', port=6379):
        self.client = redis.StrictRedis(host, port)

    def count_page(self, author, page='all'):
        self.client.incr(author + ':' + page)

    def query_page(self, author, page='all'):
        try:
            count = self.client.get(author + ':' + page)
            return int(count)
        except Exception:
            print(f'{author}的{page}页面还没被访问过或者不存在。。。')
            return 0


def main():
    # pagecounter = PageCounter()
    # pagecounter.count_page('lee', 'home')
    # pagecounter.count_page('lee', 'home')
    # pagecounter.count_page('lee', 'home')
    # count = pagecounter.query_page('lee', 'home')
    # print(count)
    # count = pagecounter.query_page('lee', 'home1')
    pass


if __name__ == "__main__":
    main()
