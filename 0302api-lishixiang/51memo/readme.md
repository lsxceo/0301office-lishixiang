# 51memo

> Author: Lishixiang

## 作业要求

一、为备忘录添加如下功能：

1. 添加记录时，时间格式统一为： 年-月-日 时：分：秒；
2. 增加查询接口，可以根据月份返回json数据；
3. 增加邮件发送接口，根据输入内容选择发送整月或整年数据给特定人物；
4. 所有功能可以通过命令行参数形式调用；
5. 整个工程包含多个目录，包含配置文件，日志记录，数据文件。

### 完成情况

皆已完成

### 运行结果

```
(lishixiang) C:\Users\LuSai\51cto-task>C:/Users/LuSai/Anaconda3/envs/lishixiang/python.exe c:/Users/LuSai/51cto-task/0302office-lishixiang/51memo/bin/main.py
**********欢迎使用备忘录系统***********
***********欢迎进入登录界面***********
请输入账号(exit退出)： admin
请输入密码：admin
2019-10-10 23:45:20,760 memoadmin.py [line:98] memo_log.log INFO 验证成功！
登录成功！
--------Admin欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: month_query
6: export_pdf
7: mail_send
q: quit
请输入要操作的菜单：1
请输入要添加的备忘事项：(示例：明天下午2点开会@小李@小王)下周五晚上6点吃火锅@小周@小李
2019-10-10 23:46:02,785 memoadmin.py [line:146] memo_log.log WARNING 新增备忘条目：2019-10-11 18:00:00 吃火锅@小周@小李
--------Admin欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: month_query
6: export_pdf
7: mail_send
q: quit
请输入要操作的菜单：5                            
--------------------
请输入要查询的月份：10
[{"id": 1, "time_": "2019-10-11 14:00:00", "thing": "\u5f00\u4f1a", "name": ["\u5c0f\u674e", "\u5c0f\u738b"]}, {"id": 2, "time_": "2019-10-12 14:00:00", "thing": "\u5f00\u4f1a", "name": ["\u5c0f\u674e", "\u5c0f\u738b"]}, {"id": 3, "time_": "2019-10-16 19:00:00", "thing": "\u770b\u7535\u5f71", "name": ["\u5c0f\u5362"]}, {"id": 5, "time_": "2019-10-12 19:00:00", "thing": "\u770bRNG\u7684\u6bd4\u8d5b", "name": ["\u6211"]}, {"id": 6, "time_": "2019-10-11 19:00:00", "thing": "\u770b\u7535\u5f71", "name": ["\u5c0f\u5362"]}, {"id": 7, "time_": "2019-10-11 18:00:00", "thing": "\u5403\u706b\u9505", "name": ["\u5c0f\u5468", "\u5c0f\u674e"]}]
--------Admin欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: month_query
6: export_pdf
7: mail_send
q: quit
请输入要操作的菜单：7
请选择需要发送整月还是整年的数据：  
1: month
2: year
请输入前面的数字（‘q’退出）：2
请输入年份：2019
2019-10-11 14:00:00 开会@小李@小王
2019-10-12 14:00:00 开会@小李@小王
2019-10-16 19:00:00 看电影@小卢
2019-11-04 18:00:00 庆生@小卢
2019-10-12 19:00:00 看RNG的比赛@我
2019-10-11 19:00:00 看电影@小卢
2019-10-11 18:00:00 吃火锅@小周@小李
2019-11-07 18:00:00 看某明星演唱会@我

2019-10-10 23:55:31,133 memoadmin.py [line:270] memo_log.log WARNING 给admin的邮件发送成功！
--------Admin欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: month_query
6: export_pdf
7: mail_send
q: quit
请输入要操作的菜单：
```

配置
```
[DEFAULT]
base_dir = c:\Users\LuSai\51cto-task\0301office-lishixiang\51memo
db_type = pkl

[admin]
db_path = ${base_dir}/db
db_type = pkl
db_name = admin.pkl
email = 214842382@qq.com
```

邮件收件箱截图
![QQ20191010235920](C:\Users\LuSai\Pictures\QQ20191010235920.png)

## 学习总结

在写这个工程项目时，因为和我上次的版本相差蛮多，所以有些函数重新写了，比如create_event.py中我加入了‘下周’，‘下个月’可以作为创建备忘录条目的关键词，然后时间格式也重新进行了优化，本来分成日期，时间段，小时，分钟的现在直接用‘年-月-日 时：分：秒’格式化显示，去掉了时间段显示，不过时间段还是作为区分12小时制习惯时作为关键词需要放入人工录入的备忘录时。