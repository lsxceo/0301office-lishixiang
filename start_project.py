#!usr/bin/env python
# -*- coding:utf-8 -*-
# statr_project.py
# author: lishixiang


import os
import sys

function = """
针对上次作业的MemoAdmin类;
1. 添加注册和登录功能,用户名密码使用dict保存为: users.pkl.
2. 添加配置文件, 为备忘录数据指定路径, 类型和文件名.比如zhangsan, 则数据文件可以为zhangsan.pkl或zhangsan.db.
3. 注册时, 相应数据文件根据用户名在配置文件保存为新的section。
4. 启动程序先提示登录，每次登录时候，先根据配置文件读取用户信息，找不到则提示注册。
5. 导出文件功能，将历史数据导出文pdf文件。
6. 对每一个函数操作添加日志功能，并在需要时候随时关闭。
"""

__author__ = 'lishixiang'
path = os.path.dirname(os.path.abspath(__file__))


def start_project():
    # 从命令行参数取工程名， 默认为memo_program
    project_name = '51memo'
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

    # 创建目录， readme, __init__文件
    folders = ['bin', 'conf', 'core', 'db', 'log']
    for folder in folders:
        folder_path = os.path.join(path, project_name, folder)
        print(folder_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # readme
        with open(os.path.join(path, project_name, 'readme.md'), 'w', encoding='utf-8') as f:
            f.write('# ' + project_name + '\n\n')
            f.write('> Author: ' + __author__.title() + '\n\n')
            f.write(function)
        # add init file
        with open(os.path.join(path, project_name, folder, '__init__.py'), 'w'):
            pass


def main():
    start_project()

if __name__ == "__main__":
    main()