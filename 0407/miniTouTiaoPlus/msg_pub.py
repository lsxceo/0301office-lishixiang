#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# msg_pub.py


from basemq import BaseMQ
from admin import TouTiao


class PubMQ(BaseMQ):
    def __init__(self):
        super().__init__()
        self.toutiao = TouTiao()
        self.args = self.toutiao.args

    def toutiao_parse(self):
        """启动CLI工具的主要功能"""
        if self.args.show is True:
            self.toutiao.show_data()
        if self.args.add:
            tuple_add = self.toutiao.add()
            msg = self.title_msg(tuple_add[0], tuple_add[1], tuple_add[2])
            return msg
            # self.make_exchange(exchange='title', exchange_type='fanout')
            # self.publish(msg, 'title')
            # print(f"发送消息：{msg}")
        if self.args.delete:
            self.toutiao.delete()
        if self.args.show is not True and self.args.add is None and self.args.delete is None:
            self.toutiao.parse.print_help()
        return False

    def title_msg(self, author, title, content):
        "发布文章"
        msg = f"{author}发布了新文章'{title}',主要内容是'{content}'..."
        return msg


def main():
    mq_pub = PubMQ()
    msg = mq_pub.toutiao_parse()  # 启动后进行一遍命令行工具操作
    if msg:
        mq_pub.make_exchange(exchange='news', exchange_type='fanout')
        mq_pub.publish(msg, 'news')
        print(f"发送消息：{msg}")


if __name__ == "__main__":
    main()
