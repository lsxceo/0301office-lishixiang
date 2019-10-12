# imageutil

> Author: Lishixiang

## 二、制作图像处理类，命名为ImageUtils,添加如下功能：

- 给定目录，选取目录中所有图片类型文件（jpg, png, bmp），并用excel存档：第一列文件名，第二列文件大小；
- 可根据命令行参数，对图像进行旋转，裁剪操作；
- 整个工程包含多个目录，包含配置文件，日志记录，数据文件；
- （选做）添加任何图片相关的好玩功能。

## 完成情况

- 对选定目录可以进行Excel存档，第一列文件名，第二列文件大小，第三列绝对路径，第四列缩略图。
- 可以用命令行参数对当前目录下的指定文件进行旋转和裁剪操作。
- 整个工程包含多个目录，包含配置文件，日志记录，数据文件。

## 终端展示

```
(lishixiang) C:\Users\LuSai\51cto-task>C:/Users/LuSai/Anaconda3/envs/lishixiang/python.exe c:/Users/LuSai/51cto-task/0302office-lishixiang/imageutil/bin/main.py
2019-10-12 15:10:09,314 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,318 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,324 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,328 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,337 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,344 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,350 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,354 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,365 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,374 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,380 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,388 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,400 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,406 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,422 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,444 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,487 imageutils.py [line:72] common_log WARNING 图片信息已写入Excel！

(lishixiang) C:\Users\LuSai\51cto-task>

```

命令行参数演示
```
c:\Users\LuSai\51cto-task\0302office-lishixiang\imageutil\bin>C:/Users/LuSai/Anaconda3/Scripts/activate

(base) c:\Users\LuSai\51cto-task\0302office-lishixiang\imageutil\bin>conda activate lishixiang

(lishixiang) c:\Users\LuSai\51cto-task\0302office-lishixiang\imageutil\bin>python main.py crop_image c2cec3fdfc.jpg
2019-10-12 15:13:25,790 imageutils.py [line:80] common_log WARNING 图像裁剪成功！

(lishixiang) c:\Users\LuSai\51cto-task\0302office-lishixiang\imageutil\bin>python main.py rotate_image c2cec3fdfc.jpg
2019-10-12 15:13:49,712 imageutils.py [line:86] common_log WARNING 对图像进行了旋转操作！

(lishixiang) c:\Users\LuSai\51cto-task\0302office-lishixiang\imageutil\bin>
```

配置文件

```
[DEFAULT]
base_dir = c:\Users\LuSai\51cto-task\0302office-lishixiang\imageutil
db_type = xlsx

[imageutils]
box = (100, 100, 400, 400)
angle = 90
percent = 0.1


```

日志文件

```
2019-10-12 15:10:09,314 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,318 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,324 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,328 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,337 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,344 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,350 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,354 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,365 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,374 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,380 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,388 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,400 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,406 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,422 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,444 imageutils.py [line:38] common_log WARNING 缩放图像已保存！
2019-10-12 15:10:09,487 imageutils.py [line:72] common_log WARNING 图片信息已写入Excel！
2019-10-12 15:13:25,790 imageutils.py [line:80] common_log WARNING 图像裁剪成功！
2019-10-12 15:13:49,712 imageutils.py [line:86] common_log WARNING 对图像进行了旋转操作！

```

## 总结

在写ImageUtils图像处理类时，首先需要把图像处理的一些基本函数运用起来，然后添加到类中，此处还用到Excel和os的一些知识，都需要慢慢添加进函数中，然后把功能完善，最后把通用的配置函数和日志记录函数添加到工程中进行调试。