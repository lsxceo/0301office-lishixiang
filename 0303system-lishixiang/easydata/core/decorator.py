#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# decorator.py


import os
import json
import logging
from functools import wraps


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def log(ch_level=logging.WARNING, fh_level=logging.DEBUG):
    logger = logging.getLogger('common_log')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')
    # 控制台的日志操作
    ch = logging.StreamHandler()
    ch.setLevel(ch_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # 文件的日志操作
    log_file = os.path.join(base_dir, 'log', 'log.log')
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')
    fh.setLevel(fh_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


logger = log()


def deco_log(content='', level='warning', ch_level=logging.WARNING, fh_level=logging.DEBUG):
    """日志装饰器"""
    def wrapper(func):
        @wraps(func)
        def deco(*args, **kwargs):
            result = func(*args, **kwargs)
            if hasattr(logger, level):
                log_func = getattr(logger, level)
                if type(result) == str:
                    log_func(f'{result}{content}')
                return True
        return deco
    return wrapper


class Deco_Auth:
    """简易的验证登录程序"""
    def __init__(self, cls, num=3):
        self.login_status = False
        self.__cls = cls
        self.user_info = {}
        self.num = num

    def __call__(self, *args, **kwargs):
        if not self.login_status:
            self.menu()
            cls = self.__call__(self, *args, **kwargs)
        else:
            cls = self.__cls(user_info=self.user_info)
        return cls

    def menu(self, *args, **kwargs):
        """菜单"""
        self.num = 3
        mn = {
            '1': '登录',
            '2': '注册',
            'q': '退出'
        }
        print('数据系统主界面'.center(30, '*'))
        for k, v in mn.items():
            print(f'{k} -> {v}')
        if not self.login_status:
            choose = input('请选择： ')
            if choose == '1':
                return self.login()
            elif choose == '2':
                return self.register()
            elif choose.title() == 'Q':
                exit()
            else:
                print('输入有误，请重新输入！')

    @deco_log(content='已登录', level='debug')
    def login(self, *args):
        """用户验证"""
        # admin_json_path = os.path.join(base_dir, 'db', 'admin.json')
        # if not os.path.exists(admin_json_path):
        #     adminjson = {
        #         "username": "admin",
        #         "password": "admin",
        #         "type": "admin",
        #         "operation": ["picture_crawler", "imageutils", "authorization", "defriend"]
        #     }
        #     with open(admin_json_path, 'w') as f:
        #         json.dump(adminjson, f)
        print('登录验证'.center(30, '-'))
        username = input('username: ')
        password = input('password: ')
        json_path = os.path.join(base_dir, 'db', f'{username}.json')
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                data = json.load(f)
            if data.get('enabled', 1) == 0:
                print('此用户以为添加到黑名单，禁止登录！')
                self.num -= 1
                if self.num > 0:
                    return self.login()
                else:
                    print('再见！')
                    exit()
            elif password == data['password']:
                print('密码正确!')
                self.user_info = data
                self.login_status = True
                return username
            else:
                print('密码错误!')
                self.num -= 1
                if self.num > 0:
                    return self.login()
                else:
                    print('密码输入错误3次，返回主界面')
                    return self.menu()
        else:
            print('用户名不存在, 是否需要注册？')
            option = input("'y'确认, 'q'退出, 按其他返回： ").upper()
            if option == 'Y':
                return self.register()
            elif option == 'Q':
                exit()
            else:
                return self.login()

    @deco_log('已注册')
    def register(self, *args, **kwargs):
        """注册账户"""
        print('注册账户'.center(30, '-'))
        username = input('请输入用户名(按q退出): ')
        if username.title() == 'Q':
            exit()
        elif username == '':
            print('用户名不能为空，请重新输入')
            return self.register(*args, **kwargs)
        elif os.path.exists(os.path.join(base_dir, 'db', f'{username}.json')):
            print(f'{username}已存在，请重新输入')
            return self.register(*args, **kwargs)
        else:
            password = input('请输入密码: ')
            password_check = input('请确认密码: ')

        if password == password_check:
            dic = {}
            dic['username'] = username
            dic['password'] = password
            dic['type'] = 'user'
            dic['operation'] = []
            dic['enabled'] = 1
            with open(os.path.join(base_dir, 'db', f'{username}.json'), 'w') as f:
                json.dump(dic, f)
            return username
        else:
            print('两次密码不一致，请重新输入')
            return self.register()
        return self.menu()
