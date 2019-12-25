#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# imageutils.py


import os
from PIL import Image


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ImageSystem:
    """照片管理系统"""
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir

    def thumbnail(self, filename, percent=0.5):
        "做个缩略图"
        # 打开一个jpg图像文件
        im = Image.open(os.path.join(self.source_dir, filename))
        print(im.format, im.size, im.mode)
        # 获得图像尺寸：
        w, h = im.size
        print('尺寸: %sx%s' % (w, h))
        # 缩放到50%：
        im.thumbnail((int(w*percent), int(h*percent)))
        # 把缩放后的图像用jpeg格式保存：
        im.save(os.path.join(self.target_dir, filename.split('.')[0] + '-thumbnail.jpg'), 'jpeg')
        print('图片已保存')

    def watermark(self, filename, logo_file='logo.jpg'):
        "添加水印"
        # 添加水印，复制图片，计算位置，粘贴合并图片
        # 打开logo文件
        # logo_file = 'timg.jpg'
        im_logo = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), logo_file))
        logo_width, logo_height = im_logo.size

        # 打开目标文件
        # filename = '70.jpg'
        im_filename = Image.open(os.path.join(self.source_dir, filename))
        filename_width, filename_height = im_filename.size

        # 粘贴
        im_copy = im_filename.copy()
        im_copy.paste(im_logo, (filename_width-logo_width, filename_height-logo_height))
        im_copy.save(os.path.join(self.target_dir, filename.split('.')[0] + 'watermark.jpg'), 'jpeg')
        print('图片已保存')


def main():
    image = ImageSystem(r'C:\study\py2019\02-auto\image_ctrl', r'C:\study\py2019\02-auto\image_ctrl\target_dir')
    # image.thumbnail('70.jpg')
    image.watermark('70.jpg')


if __name__ == "__main__":
    main()
