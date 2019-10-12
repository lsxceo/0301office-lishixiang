#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# main.py


import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core import imageutils


def main():
    """主启动程序"""
    from_path = r'C:\Users\LuSai\Pictures\image_ctrl'
    to_path = r'C:\Users\LuSai\Pictures\to_path'
    imageutil = imageutils.ImageUtils(from_path, to_path)
    if len(sys.argv) > 1:
        func = getattr(imageutil, sys.argv[1])
        func(sys.argv[2])
    else:
        imageutil.write_excel()


if __name__ == "__main__":
    main()
