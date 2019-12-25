仿照51备忘录目录结构和功能，做一个简易数据处理系统，在数据抓取，分析，office文件操作，图片操作等功能，至少选择2项功能，每一项提供至少2个操作函数，多多益善，具体需求如下：

# 任务要求

- 使用装饰器完成登录验证，用户不存在，则提示注册
- 用户数据保存为：用户名.json，管理员默认为admin.json
- 用户分为两种类型：管理员，普通用户，作为一个字段type，具体值为admin或user，保存到：用户名.json
- 操作菜单根据用户角色显示不同：
    - 管理员可以看见所有操作，除登录外，数据相关操作根据json数据里的列表("operation":["crawler", "office", "image"])进行菜单展示。
    - 普通用户默认只有登录，注册功能，登录后数据操作列表默认为空，需要管理员操作授权，再次登录时候显示被授权的操作
- 每一次操作要有日志记录到文件和控制台，但日志等级不同，文件的为DEBUG，控制台的为WARNING
- 要有完整的各个功能运行截图和测试数据

# 流程截图

```
LuSai@LAPTOP-DFHOK32H C:\Users\LuSai
$ conda activate py38

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai
$ cd C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: admin
password: admin
密码正确!
系统初始化
**********欢迎登录管理员系统***********
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)q

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 2
-------------注册账户-------------
请输入用户名(按q退出): lsx
请输入密码: lsx
请确认密码: lsx
2019-12-25 18:35:07,318 decorator.py [line:45] common_log WARNING lsx已注册
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: lsx
password: lsx
密码正确!
系统初始化
************欢迎登录系统************
没有可操作的功能，叫管理员授权

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: admin
password: admin
密码正确!
系统初始化
**********欢迎登录管理员系统***********
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)3
请输入要授权的用户(q退出)：lsx
目前所有权限如下：
 ['picture_crawler', 'imageutils']
请输入要授予的功能(q退出)：picture_crawler
授权已完成
2019-12-25 18:35:42,131 decorator.py [line:45] common_log WARNING lsx -> picture_crawler已授权
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)3
请输入要授权的用户(q退出)：lsx
目前所有权限如下：
 ['picture_crawler', 'imageutils']
请输入要授予的功能(q退出)：imageutils
授权已完成
2019-12-25 18:35:52,445 decorator.py [line:45] common_log WARNING lsx -> imageutils已授权
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)q

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: lsx
password: lsx
密码正确!
系统初始化
************欢迎登录系统************
------------------------------
1 -> imageutils
2 -> picture_crawler
------------------------------
请输入需要操作的功能(q退出)1
1 -> 做个缩略图
2 -> 添加水印
q -> 退出
请输入需要操作的功能(q退出)：1
请输入源文件所在目录:C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\
db
请输入输出文件所在目录:C:\Users\LuSai\51cto-task\0303system-lishixiang\easydat
a\db
请输入文件名：32.jpg
JPEG (640, 640) RGB
尺寸: 640x640
图片已保存
2019-12-25 18:36:53,554 decorator.py [line:45] common_log WARNING lsx -> 32.jpg缩略图已完成
------------------------------
1 -> imageutils
2 -> picture_crawler
------------------------------
请输入需要操作的功能(q退出)2
1 -> 爬取子页中的所有图片
2 -> 根据输入名字爬取所有照片
q -> 退出
请选择需要操作的功能（q退出）：1
请输入需要爬虫的网页(Referer网页子页)：https://www.meitulu.com/item/18048.html

Downloading: https://www.meitulu.com/item/18048.html
name: 莫晓希
num: 9
id: 18048
pic_num: 0
下载图片： https://mtl.gzhuibei.com/images/img/18048/1.jpg 莫晓希 1
下载图片： https://mtl.gzhuibei.com/images/img/18048/2.jpg 莫晓希 2
下载图片： https://mtl.gzhuibei.com/images/img/18048/3.jpg 莫晓希 3
下载图片： https://mtl.gzhuibei.com/images/img/18048/4.jpg 莫晓希 4
下载图片： https://mtl.gzhuibei.com/images/img/18048/5.jpg 莫晓希 5
下载图片： https://mtl.gzhuibei.com/images/img/18048/6.jpg 莫晓希 6
下载图片： https://mtl.gzhuibei.com/images/img/18048/7.jpg 莫晓希 7
下载图片： https://mtl.gzhuibei.com/images/img/18048/8.jpg 莫晓希 8
下载图片： https://mtl.gzhuibei.com/images/img/18048/9.jpg 莫晓希 9
2019-12-25 18:42:05,913 decorator.py [line:45] common_log WARNING lsx -> https://www.meitulu.com/item/18048.html下载完成
------------------------------
1 -> imageutils
2 -> picture_crawler
------------------------------
请输入需要操作的功能(q退出)1
1 -> 做个缩略图
2 -> 添加水印
q -> 退出
请输入需要操作的功能(q退出)：q

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: lsx
password: lsx
密码正确!
系统初始化
************欢迎登录系统************
------------------------------
1 -> imageutils
2 -> picture_crawler
------------------------------
请输入需要操作的功能(q退出)2
1 -> 爬取子页中的所有图片
2 -> 根据输入名字爬取所有照片
q -> 退出
请选择需要操作的功能（q退出）：2
请输入美女名字：美伊
Downloading: https://www.meitulu.com/search/美伊
Downloading: https://www.meitulu.com/item/18052.html
name: 美伊
num: 8
id: 18052
pic_num: 0
下载图片： https://mtl.gzhuibei.com/images/img/18052/1.jpg 美伊 1
下载图片： https://mtl.gzhuibei.com/images/img/18052/2.jpg 美伊 2
下载图片： https://mtl.gzhuibei.com/images/img/18052/3.jpg 美伊 3
下载图片： https://mtl.gzhuibei.com/images/img/18052/4.jpg 美伊 4
下载图片： https://mtl.gzhuibei.com/images/img/18052/5.jpg 美伊 5
下载图片： https://mtl.gzhuibei.com/images/img/18052/6.jpg 美伊 6
下载图片： https://mtl.gzhuibei.com/images/img/18052/7.jpg 美伊 7
下载图片： https://mtl.gzhuibei.com/images/img/18052/8.jpg 美伊 8
Downloading: https://www.meitulu.com/item/18051.html
name: 美伊
num: 28
id: 18051
pic_num: 8
下载图片： https://mtl.gzhuibei.com/images/img/18051/1.jpg 美伊 9
下载图片： https://mtl.gzhuibei.com/images/img/18051/2.jpg 美伊 10
下载图片： https://mtl.gzhuibei.com/images/img/18051/3.jpg 美伊 11
下载图片： https://mtl.gzhuibei.com/images/img/18051/4.jpg 美伊 12
下载图片： https://mtl.gzhuibei.com/images/img/18051/5.jpg 美伊 13
下载图片： https://mtl.gzhuibei.com/images/img/18051/6.jpg 美伊 14
下载图片： https://mtl.gzhuibei.com/images/img/18051/7.jpg 美伊 15
下载图片： https://mtl.gzhuibei.com/images/img/18051/8.jpg 美伊 16
下载图片： https://mtl.gzhuibei.com/images/img/18051/9.jpg 美伊 17
下载图片： https://mtl.gzhuibei.com/images/img/18051/10.jpg 美伊 18
Traceback (most recent call last):
  File "main.py", line 36, in <module>
    main()
  File "main.py", line 32, in main
    Login()
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\decorator.py", line 62, in __call__
    cls = self.__call__(self, *args, **kwargs)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\decorator.py", line 64, in __call__
    cls = self.__cls(user_info=self.user_info)
  File "main.py", line 21, in __init__
    self.main()
  File "main.py", line 28, in main
    User(self.user_info)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\login.py", line 190, in __init__
    self.main()
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\login.py", line 205, in main
    func()
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\decorator.py", line 41, in deco
    result = func(*args, **kwargs)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\login.py", line 45, in picture_crawler
    mtldownload.find_all(name)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\picture_crawler.py", line 139, in find_all
    self.find_picturl_by_url(url, headers=headers)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\picture_crawler.py", line 127, in find_picturl_by_url
    self.picture_download(url.format(id, str(i)), name, str(i + pic_num), headers=headers)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\picture_crawler.py", line 71, in picture_download
    self.throttle.wait(url)
  File "C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\core\picture_crawler.py", line 38, in wait
    time.sleep(sleep_secs)
KeyboardInterrupt
^C
> 可以跳页下载，因为下载的太多了所以强制停止了

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: admin
password: admin
密码正确!
系统初始化
**********欢迎登录管理员系统***********
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)4
请输入需要操作的用户名(q退出)：lsx
lsx现在是白名单，是否要添加到黑名单（y/n）y
2019-12-25 18:44:43,911 decorator.py [line:45] common_log WARNING lsx已被添加
到黑名单
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)4
请输入需要操作的用户名(q退出)：lsx
lsx现在是黑名单，是否要添加到白名单（y/n）n
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)q

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: lsx
password: lsx
此用户以为添加到黑名单，禁止登录！
-------------登录验证-------------
username: lsx
password: lsx
此用户以为添加到黑名单，禁止登录！
-------------登录验证-------------
username: admin
password: admin
密码正确!
系统初始化
**********欢迎登录管理员系统***********
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)4
请输入需要操作的用户名(q退出)：lsx
lsx现在是黑名单，是否要添加到白名单（y/n）y
2019-12-25 18:45:22,972 decorator.py [line:45] common_log WARNING lsx已被添加
到白名单
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)q

(py38) LuSai@LAPTOP-DFHOK32H C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\bin
$ python main.py
***********数据系统主界面************
1 -> 登录
2 -> 注册
q -> 退出
请选择： 1
-------------登录验证-------------
username: admin
password: admin
密码正确!
系统初始化
**********欢迎登录管理员系统***********
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)2
1 -> 做个缩略图
2 -> 添加水印
q -> 退出
请输入需要操作的功能(q退出)：1
请输入源文件所在目录:C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\
db
请输入输出文件所在目录:C:\Users\LuSai\51cto-task\0303system-lishixiang\easydat
a\db
请输入文件名：32.jpg
JPEG (640, 640) RGB
尺寸: 640x640
图片已保存
2019-12-25 18:50:51,148 decorator.py [line:45] common_log WARNING admin -> 32.jpg缩略图已完成
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)2
1 -> 做个缩略图
2 -> 添加水印
q -> 退出
请输入需要操作的功能(q退出)：2
请输入源文件所在目录:C:\Users\LuSai\51cto-task\0303system-lishixiang\easydata\
db
请输入输出文件所在目录:C:\Users\LuSai\51cto-task\0303system-lishixiang\easydat
a\db
请输入文件名：32.jpg
图片已保存
2019-12-25 18:51:11,963 decorator.py [line:45] common_log WARNING admin -> 32.jpglogo制作完成
------------------------------
1 -> picture_crawler
2 -> imageutils
3 -> authorization
4 -> defriend
------------------------------
请输入要操作的功能(q退出)q

```

# 日志的显示

    登录功能的level设置成'debug', 所以在控制台中没有输出登录信息，日志里打印了登录信息

```
2019-12-25 18:34:32,958 decorator.py [line:45] common_log DEBUG admin已登录
2019-12-25 18:35:07,318 decorator.py [line:45] common_log WARNING lsx已注册
2019-12-25 18:35:16,289 decorator.py [line:45] common_log DEBUG lsx已登录
2019-12-25 18:35:29,131 decorator.py [line:45] common_log DEBUG admin已登录
2019-12-25 18:35:42,131 decorator.py [line:45] common_log WARNING lsx -> picture_crawler已授权
2019-12-25 18:35:52,445 decorator.py [line:45] common_log WARNING lsx -> imageutils已授权
2019-12-25 18:36:07,169 decorator.py [line:45] common_log DEBUG lsx已登录
2019-12-25 18:36:53,554 decorator.py [line:45] common_log WARNING lsx -> 32.jpg缩略图已完成
2019-12-25 18:42:05,913 decorator.py [line:45] common_log WARNING lsx -> https://www.meitulu.com/item/18048.html下载完成
2019-12-25 18:43:07,611 decorator.py [line:45] common_log DEBUG lsx已登录
2019-12-25 18:44:33,729 decorator.py [line:45] common_log DEBUG admin已登录
2019-12-25 18:44:43,911 decorator.py [line:45] common_log WARNING lsx已被添加到黑名单
2019-12-25 18:45:18,120 decorator.py [line:45] common_log DEBUG admin已登录
2019-12-25 18:45:22,972 decorator.py [line:45] common_log WARNING lsx已被添加到白名单
2019-12-25 18:50:04,603 decorator.py [line:45] common_log DEBUG lsx已登录
2019-12-25 18:50:20,283 decorator.py [line:45] common_log DEBUG admin已登录
2019-12-25 18:50:51,148 decorator.py [line:45] common_log WARNING admin -> 32.jpg缩略图已完成
2019-12-25 18:51:11,963 decorator.py [line:45] common_log WARNING admin -> 32.jpglogo制作完成

```