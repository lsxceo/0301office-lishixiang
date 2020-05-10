#!usr/bin/env Python
# -*- coding: utf-8 -*-
# msg_worker.py


from basemq import BaseMQ


class WorkerMQ(BaseMQ):
    "消费端，负责接收消息"
    def __init__(self):
        super().__init__()

    def callback(self, ch, method, properties, body):
        print(f"收到消息：{body.decode()}")
        ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    mq_con = WorkerMQ()
    mq_con.make_exchange(exchange='news', exchange_type='fanout')
    q_name = mq_con.make_random_queue()
    mq_con.bind_queue(q_name, 'news')
    mq_con.consume(mq_con.callback, q_name)


if __name__ == "__main__":
    main()
