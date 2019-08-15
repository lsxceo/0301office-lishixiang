import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import memoadmin


def main():
    print('欢迎使用备忘录系统'.center(30, '*'))
    admin = memoadmin.MemoAdmin()
    user = admin.login()
    admin.choose_menu(user)


if __name__ == '__main__':
    main()
    