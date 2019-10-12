#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# main.py
# author: lishixiang

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core import memoadmin


def main():
    "主启动程序"
    print('欢迎使用备忘录系统'.center(30, '*'))
    admin = memoadmin.MemoAdmin()
    user = admin.login()
    if len(sys.argv) > 1:
        name = sys.argv[1]
        func = getattr(admin, name)
        func(user)
    else:
        admin.choose_menu(user)


if __name__ == '__main__':
    main()
