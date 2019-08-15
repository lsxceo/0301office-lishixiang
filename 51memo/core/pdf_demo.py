# pdf_demo.py
# coding: utf-8
# de8ug
# 需要提前安装：pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('simsun', 'C:\WINDOWS\Fonts\simsun.ttc'))  # 导入字体文件，使用Windows字体或下载好的"simsun.ttf"，用来显示中文


class ExportPDF:
    """
    Export a pdf file based on reportlab
    把要处理的文本result_list写成pdf文件
    """
    def __init__(self, result_list, output_path='log_out.pdf', is_custom_color=False, color=(0.77, 0.77, 0.77), font_size=8, offset_x=5, offset_y=5):
        self.result_list = result_list
        self.output_path = output_path
        self.is_custom_color = is_custom_color
        self.font_size = font_size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.color = color

    def save_string(self):
        """使用canvas把数据绘制到pdf文件，默认坐标从左下角开始，与屏幕坐标（右上角开始）相反，所以需要单独处理
        """
        c = canvas.Canvas(self.output_path, pagesize=A4)
        width, height = A4  # 使用默认的A4大小

        if self.is_custom_color:
            c.setFillColorRGB(self.color)  # 需要单独设置颜色时候使用

        new_height = height
        for line in self.result_list:
            c.setFont("simsun", self.font_size)  # 处理中文字体
            # 写入每一行的数据，每一行的y坐标需要单独处理，这里用总高度减去偏移量和字体高度，使得每一行依次写入文件
            new_height = new_height - self.offset_y - self.font_size
            print('write data: ', self.offset_x, new_height, line)
            c.drawString(self.offset_x, new_height, line)

        c.showPage()
        c.save()

    def save_text(self):
        """使用canvas把数据绘制到pdf文件，
        这是另一种写法，通过文本的方式写入，只需要定义原始写入坐标
        """
        c = canvas.Canvas(self.output_path, pagesize=A4)
        width, height = A4  # 使用默认的A4大小

        if self.is_custom_color:
            c.setFillColorRGB(self.color)  # 需要单独设置颜色时候使用

        c.setFont("simsun", self.font_size)  # 处理中文字体
        obj = c.beginText()  # 生成text对象
        obj.setTextOrigin(10, height-self.offset_y*20)  # 第一次写入位置，坐标自定义,注意高度需要调整
        for line in self.result_list:
            print('write data: ', line)
            obj.textLine(line)  # 写入文件

        c.drawText(obj)
        c.showPage()
        c.save()


def main():
    result_list = ['line1', 'line2', 'line3中文', 'line4继续']
    pdf = ExportPDF(result_list)
    # pdf.save_string()
    pdf.save_text()


if __name__ == "__main__":
    main()