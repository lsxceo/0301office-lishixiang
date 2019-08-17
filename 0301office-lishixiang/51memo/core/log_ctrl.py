#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# log_ctrl.py
# author: lishixiang


import logging
import os
import sys


"""
工程使用需求：
1-不同日志名称
2-打印同时在控制台，也有文件
3-灵活控制等级
"""

base_dir = os.path.dirname(os.path.abspath(__file__))


def common_log(logger_name='common_log', log_file=os.path.join(base_dir, 'log', 'test.log'), level=logging.WARNING):
    # logging.disable(logging.CRITICAL)  # 禁止所有日志输出
    # 创建logger对象
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # 创建控制台 console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # 创建文件
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')

    # 创建formatter
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')

    # 添加formatter
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把ch, fh 添加到logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

def main():
    # test
    logger = common_log()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    main()
    
