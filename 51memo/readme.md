# 51memo

> Author: Lishixiang

## 作业要求

针对上次作业的MemoAdmin类;

1. 添加注册和登录功能,用户名密码使用dict保存为: users.pkl.
2. 添加配置文件, 为备忘录数据指定路径, 类型和文件名.比如zhangsan, 则数据文件可以为zhangsan.pkl或zhangsan.db.
3. 注册时, 相应数据文件根据用户名在配置文件保存为新的section。
4. 启动程序先提示登录，每次登录时候，先根据配置文件读取用户信息，找不到则提示注册。
5. 导出文件功能，将历史数据导出为pdf文件。
6. 对每一个函数操作添加日志功能，并在需要时候随时关闭。

## 完成情况

1. 运行带有命令行参数的start_project.py文件创建51memo工程目录。
2. core文件夹中创建configadmin.py, create_event.py, log_ctrl.py, memo.py, memoadmin.py, setting.py, 并复制了输出pdf文件的代码文件pdf_demo.py和SimSun.ttf。  
3. 在bin文件夹中创建了main.py，负责启动程序。

## 运行结果

```cmd
(lishixiang) C:\study\0301office-lishixiang>C:/Users/LuSai/Anaconda3/envs/lishixiang/python.exe c:/study/0301office-lishixiang/51memo/bin/main.py
**********欢迎使用备忘录系统***********
***********欢迎进入登录界面***********
请输入账号(exit退出)： apple
输入的账号不存在！
请输入要注册的账户名称(exit退出)：apple
请输入密码： app
请再次输入密码： appp
输入有误！请重新输入：
请输入要注册的账户名称(exit退出)：apple
请输入密码： app
请再次输入密码： app
2019-08-15 15:14:34,946 memoadmin.py [line:71] memo_log.log WARNING 新用户apple已创建
注册成功！
***********欢迎进入登录界面***********
请输入账号(exit退出)： apple
请输入密码：appp
2019-08-15 15:14:41,323 memoadmin.py [line:98] memo_log.log WARNING 密码输入错误！
***********欢迎进入登录界面***********
请输入账号(exit退出)： apple
请输入密码：app
2019-08-15 15:14:49,085 memoadmin.py [line:94] memo_log.log INFO 验证成功！
登录成功！
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：1
请输入要添加的备忘事项：(示例：明天下午2点开会@小李@小王)明天下午2点开会@小李
2019-08-15 15:14:58,269 memoadmin.py [line:143] memo_log.log WARNING 新增备忘条目：2019-08-16:下午 2:00开会@小李
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：1
请输入要添加的备忘事项：(示例：明天下午2点开会@小李@小王)后天上午6点起床
2019-08-15 15:15:13,447 memoadmin.py [line:143] memo_log.log WARNING 新增备忘条目：2019-08-17:上午 6:00起床@我
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：1
请输入要添加的备忘事项：(示例：明天下午2点开会@小李@小王)20号晚上8点看电影@小周
2019-08-15 15:15:42,481 memoadmin.py [line:143] memo_log.log WARNING 新增备忘条目：2019-08-20:晚上 8:00看电影@小周
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：4
2019-08-16:下午 2:00开会@小李
2019-08-17:上午 6:00起床@我
2019-08-20:晚上 8:00看电影@小周
- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
2019-08-15 15:16:00,414 memoadmin.py [line:201] memo_log.log INFO 查看备忘录列表
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：3
ID: 1   2019-08-16:下午 2:00开会@小李
ID: 2   2019-08-17:上午 6:00起床@我
ID: 3   2019-08-20:晚上 8:00看电影@小周
请输入你要修改的备忘事项的ID： 3
请输入修改后的事项： 20号晚上9点看电影@小周
2019-08-15 15:16:32,433 memoadmin.py [line:191] memo_log.log WARNING 备忘录修改成功！ID: 3  2019-08-20:晚上 8:00看电影@小周 修改为 2019-08-20:晚上 9:00看电影@小周
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：4
2019-08-16:下午 2:00开会@小李
2019-08-17:上午 6:00起床@我
2019-08-20:晚上 9:00看电影@小周
- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
2019-08-15 15:16:37,161 memoadmin.py [line:201] memo_log.log INFO 查看备忘录列表
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：2
ID: 1   2019-08-16:下午 2:00开会@小李
ID: 2   2019-08-17:上午 6:00起床@我
ID: 3   2019-08-20:晚上 9:00看电影@小周
请输入要删除的备忘事项的ID： 1
2019-08-15 15:16:48,094 memoadmin.py [line:156] memo_log.log WARNING 删除条目-ID: 1 2019-08-16:下午 2:00开会@小李
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：4
2019-08-17:上午 6:00起床@我
2019-08-20:晚上 9:00看电影@小周
- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
2019-08-15 15:16:51,594 memoadmin.py [line:201] memo_log.log INFO 查看备忘录列表
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：5
write data:  Apple的备忘录
write data:  2019-08-17:上午 6:00起床@我
write data:  2019-08-20:晚上 9:00看电影@小周
2019-08-15 15:17:01,559 memoadmin.py [line:213] memo_log.log WARNING 导出Apple的备忘录为PDF
--------Apple欢迎进入51备忘录--------
------------------------------
1: add
2: delete
3: modify
4: query
5: export_pdf
q: quit
请输入要操作的菜单：q

(lishixiang) C:\study\0301office-lishixiang>

```

## 结果分析

能够简单的实现备忘录的增删改查，以及导出至PDF功能，conf文件夹的admin.ini也能配置用户信息：

```ini
[DEFAULT]
base_dir = c:\study\0301office-lishixiang\51memo
db_type = pkl

[apple]
db_path = ${base_dir}/db
db_type = pkl
db_name = apple.pkl

```


log文件夹的memo_log.log文件能记录操作日志，并且在需要的情况下关闭

```python
2019-08-15 15:14:34,946 memoadmin.py [line:71] memo_log.log WARNING 新用户apple已创建
2019-08-15 15:14:41,323 memoadmin.py [line:98] memo_log.log WARNING 密码输入错误！
2019-08-15 15:14:49,085 memoadmin.py [line:94] memo_log.log INFO 验证成功！
2019-08-15 15:14:58,269 memoadmin.py [line:143] memo_log.log WARNING 新增备忘条目：2019-08-16:下午 2:00开会@小李
2019-08-15 15:15:13,447 memoadmin.py [line:143] memo_log.log WARNING 新增备忘条目：2019-08-17:上午 6:00起床@我
2019-08-15 15:15:42,481 memoadmin.py [line:143] memo_log.log WARNING 新增备忘条目：2019-08-20:晚上 8:00看电影@小周
2019-08-15 15:16:00,414 memoadmin.py [line:201] memo_log.log INFO 查看备忘录列表
2019-08-15 15:16:32,433 memoadmin.py [line:191] memo_log.log WARNING 备忘录修改成功！ID: 3  2019-08-20:晚上 8:00看电影@小周 修改为 2019-08-20:晚上 9:00看电影@小周
2019-08-15 15:16:37,161 memoadmin.py [line:201] memo_log.log INFO 查看备忘录列表
2019-08-15 15:16:48,094 memoadmin.py [line:156] memo_log.log WARNING 删除条目-ID: 1 2019-08-16:下午 2:00开会@小李
2019-08-15 15:16:51,594 memoadmin.py [line:201] memo_log.log INFO 查看备忘录列表
2019-08-15 15:17:01,559 memoadmin.py [line:213] memo_log.log WARNING 导出Apple的备忘录为PDF

```

导出的PDF文件在主目录文件夹内

```pdf
Apple的备忘录 
2019-08-17:上午 6:00起床@我 
2019-08-20:晚上 9:00看电影@小周
```

## 学习总结

起先在创建memoadmin时无法做到对其他程序的调用，后来用了from . import moduel才成功。  
我特地创建了一个setting.py文件，主要放一些路径，命名，menu之类的设置，比较直观也方便以后扩展时修改。  
