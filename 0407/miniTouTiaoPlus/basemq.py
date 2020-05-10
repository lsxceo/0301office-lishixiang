#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# basemq.py
# MQ基类


import pika
from settings import CONFIG


class BaseMQ:
    def __init__(self):
        self.connection = self.make_connect()
        self.channel = self.connection.channel()

    def make_connect(self):
        "连接服务"
        creds = pika.PlainCredentials(CONFIG["username"], CONFIG["password"])
        params = pika.ConnectionParameters(
            host=CONFIG["host"], credentials=creds)
        connection = pika.BlockingConnection(params)
        return connection

    def make_exchange(self, exchange='news', exchange_type='fanout'):
        self.channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)

    def make_random_queue(self):
        q = self.channel.queue_declare('', exclusive=True)
        return q.method.queue

    def bind_queue(self, queue, exchange, routing_key=None):
        self.channel.queue_bind(queue, exchange, routing_key)

    def make_queue(self, queue_name):
        "创建队列"
        self.channel.queue_declare(queue=queue_name, durable=True)

    def publish(self, msg, exchange, routing_key=''):
        "发送消息"
        self.channel.basic_publish(exchange=exchange, routing_key=routing_key,
                                   body=msg, properties=pika.BasicProperties(delivery_mode=2))

    def consume(self, callback, queue_name):
        "均衡任务"
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback)
        self.channel.start_consuming()

    def close_connect(self):
        "关闭连接"
        self.connection.close()
