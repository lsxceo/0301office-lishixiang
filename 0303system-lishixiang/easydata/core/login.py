#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# login.py
# 验证登录系统
# author: lishixiang


import os
import json
from .decorator import deco_log
from .picture_crawler import MtlDownload
from .imageutils import ImageSystem


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Operation:
    """功能操作类"""
    def __init__(self, username):
        self.username = username

    @deco_log('下载完成')
    def picture_crawler(self):
        "网页爬虫"
        menu = {
            '1': '爬取子页中的所有图片',
            '2': '根据输入名字爬取所有照片',
            'q': '退出'
        }
        for k, v in menu.items():
            print(f'{k} -> {v}')
        choose = input('请选择需要操作的功能（q退出）：')
        if choose.title() == 'Q':
            exit()
        elif choose == '1':
            url = input('请输入需要爬虫的网页(Referer网页子页)：')
            mtldownload = MtlDownload()
            mtldownload.find_picturl_by_url(url)
            return f'{self.username} -> {url}'
        elif choose == '2':
            name = input('请输入美女名字：')
            mtldownload = MtlDownload()
            try:
                mtldownload.find_all(name)
            except Exception as e:
                print('出错了，可能是这个名字无法查找到图片', f'错误为{e}')
                return self.picture_crawler()
            return f'{self.username} -> {name}的图片'
        else:
            print('输入有误！请重新输入。')
            return self.picture_crawler()

    @deco_log()
    def imageutils(self):
        "图片处理"
        menu = {
            '1': '做个缩略图',
            '2': '添加水印',
            'q': '退出'
        }
        for k, v in menu.items():
            print(f'{k} -> {v}')
        choose = input('请输入需要操作的功能(q退出)：')
        if choose.title() == 'Q':
            exit()
        elif choose == '1':
            try:
                soure_dir = input('请输入源文件所在目录:')
                target_dir = input('请输入输出文件所在目录:')
                filename = input('请输入文件名：')
                image = ImageSystem(soure_dir, target_dir)
                image.thumbnail(filename)
                return f'{self.username} -> {filename}缩略图已完成'
            except Exception as e:
                return f'{self.username} -> 出现错误，错误为{e}'
        elif choose == '2':
            try:
                soure_dir = input('请输入源文件所在目录:')
                target_dir = input('请输入输出文件所在目录:')
                filename = input('请输入文件名：')
                image = ImageSystem(soure_dir, target_dir)
                image.watermark(filename)
                return f'{self.username} -> {filename}logo制作完成'
            except Exception as e:
                return f'{self.username} -> 出现错误，错误为{e}'
        else:
            print('输入有误！请重新输入。')
            return self.imageutils()

    @deco_log(content='已授权')
    def authorization(self):
        """为用户授权"""
        user = input('请输入要授权的用户(q退出)：')
        permission_list = ['picture_crawler', 'imageutils']
        print('目前所有权限如下：', '\n', permission_list)
        func = input('请输入要授予的功能(q退出)：')
        if user.title() == 'Q' or func.title() == 'Q':
            exit()
        if not os.path.exists(os.path.join(base_dir, 'db', f'{user}.json')):
            print('授权的用户不存在')
            return self.authorization()
        if func not in permission_list:
            print('授予的功能输入有误')
            return self.authorization()
        with open(os.path.join(base_dir, 'db', f'{user}.json'), 'r') as f:
            data = json.load(f)
            operation_list = data['operation']
            operation_list.append(func)
            operation_list = list(set(operation_list))
            data['operation'] = operation_list
        with open(os.path.join(base_dir, 'db', f'{user}.json'), 'w') as f:
            json.dump(data, f)
        print('授权已完成')
        return f'{user} -> {func}'

    @deco_log()
    def defriend(self):
        "把普通用户添加到黑名单或白名单"
        username = input('请输入需要操作的用户名(q退出)：')
        if username.title() == 'Q':
            exit()
        if not os.path.exists(os.path.join(base_dir, 'db', f'{username}.json')):
            print(f'{username}不存在，请重新输入！')
            return self.defriend()
        with open(os.path.join(base_dir, 'db', f'{username}.json'), 'r') as f:
            data = json.load(f)
        if data['enabled'] == 1:
            ensure = input(f'{username}现在是白名单，是否要添加到黑名单（y/n）')
            if ensure.title() == 'Y':
                data['enabled'] = 0
                with open(os.path.join(base_dir, 'db', f'{username}.json'), 'w') as f:
                    json.dump(data, f)
                return f'{username}已被添加到黑名单'
        else:
            ensure = input(f'{username}现在是黑名单，是否要添加到白名单（y/n）')
            if ensure.title() == 'Y':
                data['enabled'] = 1
                with open(os.path.join(base_dir, 'db', f'{username}.json'), 'w') as f:
                    json.dump(data, f)
                return f'{username}已被添加到白名单'


class Admin:
    """管理员操作的类"""
    def __init__(self, user_info):
        print('欢迎登录管理员系统'.center(30, '*'))
        self.user_info = user_info
        self.username = self.user_info['username']
        self.oper_list = self.user_info['operation']
        self.operation = Operation(self.username)
        self.menu_dic = {}
        for index, item in enumerate(self.oper_list, 1):
            self.menu_dic[str(index)] = item
        self.main()

    def main(self):
        while True:
            print('-' * 30)
            for k, v in self.menu_dic.items():
                print(f'{k} -> {v}')
            print('-' * 30)
            choose = input('请输入要操作的功能(q退出)')
            if choose.title() == 'Q':
                exit()
            else:
                opera = self.menu_dic.get(choose, None)
                if opera:
                    func = getattr(self.operation, opera)
                    func()
                else:
                    print('输入有误，请重新输入！')
                    # return self.main()


class User:
    """用户操作类"""
    def __init__(self, user_info):
        print('欢迎登录系统'.center(30, '*'))
        self.user_info = user_info
        self.username = self.user_info['username']
        if self.user_info['operation'] == []:
            print('没有可操作的功能，叫管理员授权')
            exit()
        else:
            self.operation = Operation(self.username)
            self.menu_dic = {}
            for index, item in enumerate(self.user_info['operation'], 1):
                self.menu_dic[str(index)] = item
        self.main()

    def main(self):
        while True:
            print('-' * 30)
            for k, v in self.menu_dic.items():
                print(f'{k} -> {v}')
            print('-' * 30)
            choose = input('请输入需要操作的功能(q退出)')
            if choose.upper() == 'Q':
                exit()
            else:
                opera = self.menu_dic.get(choose, None)
                if opera:
                    func = getattr(self.operation, opera)
                    func()
                else:
                    print('输入有误，请重新输入！')
