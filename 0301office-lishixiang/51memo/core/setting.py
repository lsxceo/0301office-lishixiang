#!usr/bin/env Python
# -*- coding:utf-8 -*-
# setting.py
# author: lishixiang


import os
import logging


class Settings:
    """一个存储各种参数的类"""
    def __init__(self):
        base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.BASE_DIR = base_dir
        self.db_path = os.path.abspath(os.path.join(base_dir, 'db'))
        self.conf_path = os.path.abspath(os.path.join(base_dir, 'conf'))
        self.log_path = os.path.abspath(os.path.join(base_dir, 'log'))
        self.config_name = 'admin.ini'
        self.logger_name = 'memo_log.log'
        self.level = logging.INFO
        self.data = {
            'DEFAULT': {
                'base_dir': os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
                'db_type': 'pkl'
            }
        }
        self.menu = {
                '1': 'add',
                '2': 'delete',
                '3': 'modify',
                '4': 'query',
                '5': 'month_query',
                '6': 'export_pdf',
                '7': 'mail_send',
                'q': 'quit'
            }
        self.mail_send_choose = {
                '1': 'month',
                '2': 'year'
            }
