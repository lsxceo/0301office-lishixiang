#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# redis_sub.py


import redis
import minitoutiao as mt


class Redis_Sub:
    def __init__(self):
        self.client = redis.StrictRedis()
        self.channels = self.get_channel()

    def get_channel(self):
        "找出所有的作者作为频道名"
        changels = []
        authors = mt.session.query(mt.Author).all()
        # print("可选择的作者频道：")
        for author in authors:
            # print(author.name)
            changels.append(author.name)
        return changels

    def subscribe(self):
        "订阅频道"
        s = self.client.pubsub()
        s.subscribe(self.channels)
        for msg in s.listen():
            if msg['type'] == 'message':
                print(msg['data'].decode())


def main():
    redis_sub = Redis_Sub()
    redis_sub.subscribe()


if __name__ == "__main__":
    main()
