#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# redis_pub.py


import redis
from admin import TouTiao
import minitoutiao as mt


class Redis_Pub:
    def __init__(self):
        self.toutiao = TouTiao()
        self.client = redis.Redis()

    def toutiao_parse(self, args):
        """启动CLI工具的主要功能"""
        if args.show is True:
            self.toutiao.show_data()
        if args.add:
            author, title, content = self.toutiao.add()
            self.title_pub(author, title, content)
        if args.delete:
            self.toutiao.delete()
        if args.show is not True and args.add is None and args.delete is None:
            self.toutiao.parse.print_help()

    def get_title(self):
        "找出所有的文章"
        articles = mt.session.query(mt.Article).all()
        for article in articles:
            author = mt.session.query(mt.Author).filter(
                mt.Author.id == article.author_id).one()
            self.title_pub(author.name, article.title, article.content)

    def title_pub(self, author, title, content):
        "发布文章"
        msg = f"{author}发布了新文章'{title}',主要内容是'{content}'..."
        self.client.publish(author, msg)


def main():
    redis_pub = Redis_Pub()
    redis_pub.toutiao_parse(redis_pub.toutiao.args)  # 启动后进行一遍命令行工具操作
    # redis_pub.get_title()


if __name__ == "__main__":
    main()
