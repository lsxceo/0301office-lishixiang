#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# main.py
# author: lishixiang


import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.decorator import Deco_Auth
from core.login import User, Admin


@Deco_Auth
class Login:
    """系统初始化"""
    def __init__(self, user_info):
        print('系统初始化')
        self.user_info = user_info
        self.main()

    def main(self):
        """根据用户性质选择管理员还是普通用户界面"""
        if self.user_info['type'] == 'admin':
            Admin(self.user_info)
        else:
            User(self.user_info)


def main():
    Login()


if __name__ == '__main__':
    main()
