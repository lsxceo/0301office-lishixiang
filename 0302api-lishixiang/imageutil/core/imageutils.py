#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# imageutils.py


from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing import image
import os
import re
from . import log_ctrl, configadmin


class ImageUtils:
    """制作图像处理的类"""
    def __init__(self, from_path, to_path):
        self.from_path = from_path
        self.to_path = to_path
        self.box = (100, 100, 400, 400)
        self.angle = 90
        self.percent = 0.1
        self.logger = log_ctrl.common_log()
        self.config = configadmin.ConfigAdmin()
        self.config.add_config('imageutils', 'box', str(self.box))
        self.config.add_config('imageutils', 'angle', str(self.angle))
        self.config.add_config('imageutils', 'percent', str(self.percent))

    def thumbnail(self, file):  # file为绝对路径
        "制作缩略图"
        # im = Image.open(os.path.join(self.from_path, filename))
        im = Image.open(file)
        # 获得图像尺寸：
        w, h = im.size
        # 缩放到25%:
        im.thumbnail((int(w*self.percent), int(h*self.percent)))
        # 把缩放后的图像用jpg格式保存：
        im.save(os.path.join(self.to_path, 'thumbnail-' + os.path.basename(file)))
        self.logger.warning('缩放图像已保存！')

    def archive_file(self):
        "把图片文件归档，放入元组中，第一个文件名，第二个文件大小，第三个绝对路径"
        archive_list = []
        re_filename = re.compile('(.*jpg$)|(.*png$)|(.*bmp$)')
        for root, dirs, files in os.walk(self.from_path):
            for name in files:
                file = os.path.join(root, name)
                if re_filename.match(file):
                    self.thumbnail(os.path.abspath(file))
                    archive_list.append((name, os.path.getsize(file), os.path.abspath(file), 'thumbnail-' + name))
        return archive_list

    def write_excel(self):
        "把文件名和文件大小写入Excel"
        archive_list = self.archive_file()
        name = 'archive_image'
        wb = Workbook()
        ws1 = wb.active
        ws1.title = name
        ws1['A1'] = '文件名'
        ws1['B1'] = '文件大小'
        ws1['C1'] = '绝对路径'
        ws1['D1'] = '缩略图'
        ws1.column_dimensions['D'].width = 30
        for row in range(1, len(archive_list) + 1):
            ws1['A' + str(row + 1)] = archive_list[row - 1][0]
            ws1['B' + str(row + 1)] = archive_list[row - 1][1]
            ws1['C' + str(row + 1)] = archive_list[row - 1][2]
            img = image.Image(os.path.join(self.to_path, archive_list[row - 1][3]))
            ws1.add_image(img, 'D' + str(row + 1))
            ws1.row_dimensions[row + 1].height = 100
        wb.save(os.path.join(self.to_path, name + '.xlsx'))
        self.logger.warning('图片信息已写入Excel！')

    def crop_image(self, filename):
        "裁剪图像"
        im = Image.open(os.path.join(self.from_path, filename))
        w, h = im.size
        region = im.crop(self.box)
        region.save(os.path.join(self.to_path, filename + '-new.jpg'))
        self.logger.warning('图像裁剪成功！')

    def rotate_image(self, filename):
        "旋转图像"
        im = Image.open(os.path.join(self.from_path, filename))
        im.rotate(self.angle).save(os.path.join(self.to_path, filename + '-new.jpg'))
        self.logger.warning('对图像进行了旋转操作！')


def main():
    from_path = r'C:\Users\LuSai\Pictures\image_ctrl'
    to_path = r'C:\Users\LuSai\Pictures\to_path'
    imageutils = ImageUtils(from_path, to_path)
    # imageutils.write_excel()
    imageutils.crop_image(r'C:\Users\LuSai\Pictures\image_ctrl\0eb30f2442a7d9337.jpg')


if __name__ == "__main__":
    main()
