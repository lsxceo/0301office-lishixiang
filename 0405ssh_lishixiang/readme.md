# 程序运行过程

```shell
(py38)
LuSai@LSX MINGW64 ~/51cto-task (master)
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py
Namespace(download=False, filenames=[], shell=None, ssh=None, upload=False)
usage: LSX SSH功能列表 [-h] [-S [SSH [SSH ...]]] [-U] [-D] [-C] [filenames [filenames ...]]

positional arguments:
  filenames             文件列表，第一个表示本地文件，第二个表示远程文件

optional arguments:
  -h, --help            show this help message and exit
  -S [SSH [SSH ...]], --ssh [SSH [SSH ...]]
                        用密钥的方式登录服务器
  -U, --upload          上传文件，需要追加文件名
  -D, --download        下载文件，需要追加文件名
  -C, --shell           进入交互控制台，需要先-S登录服务器
(py38)
LuSai@LSX MINGW64 ~/51cto-task (master)
                                 usage: LSX SSH功能列表 [-h] [-S [SSH [SSH ...]]] [-U] [-D] [-C] [filenames [filenames ...]]

positional arguments:
  filenames             文件列表，第一个表示本地文件，第二个表示远程文件

optional arguments:
  -h, --help            show this help message and exit
  -S [SSH [SSH ...]], --ssh [SSH [SSH ...]]
                        用密钥的方式登录服务器
  -U, --upload          上传文件，需要追加文件名
  -D, --download        下载文件，需要追加文件名
  -C, --shell           进入交互控制台，需要先-S登录服务器
(py38)
LuSai@LSX MINGW64 ~/51cto-task (master)
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py -S
Namespace(download=False, filenames=[], shell=None, ssh=[], upload=False)
usage: LSX SSH功能列表 [-h] [-S [SSH [SSH ...]]] [-U] [-D] [-C] [filenames [filenames ...]]

positional arguments:
  filenames             文件列表，第一个表示本地文件，第二个表示远程文件

optional arguments:
  -h, --help            show this help message and exit
  -S [SSH [SSH ...]], --ssh [SSH [SSH ...]]
                        用密钥的方式登录服务器
  -U, --upload          上传文件，需要追加文件名
  -D, --download        下载文件，需要追加文件名
  -C, --shell           进入交互控制台，需要先-S登录服务器
(py38) 
LuSai@LSX MINGW64 ~/51cto-task (master)
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py -S 111.229.5.166 -C
Namespace(download=False, filenames=[], shell=True, ssh=['111.229.5.166'], upload=False)
<paramiko.client.SSHClient object at 0x000002876805CA00>
输入shell命令，q退出
>>ls -l
<paramiko.ChannelFile from <paramiko.Channel 0 (open) window=2097152 -> <paramiko.Transport at 0x6805cd00 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>>> <paramiko.ChannelFile from <paramiko.Channel 0 (open) window=2097152 -> <paramiko.Transport at 0x6805cd00 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>>>
total 44
-rw-r--r--  1 root root    72 Dec 27 23:20 1-test.ipynb
drwxr-xr-x  2 root root  4096 Dec 30 09:25 code
drwxr-xr-x 15 root root  4096 Dec 27 10:12 miniconda3
-rw-r--r--  1 root root 13129 Jan 10 16:36 ssh.log
drwxr-xr-x  3 root root  4096 Dec 27 09:33 test
-rw-r--r--  1 root root    38 Jan  9 21:55 test-new.txt

输入shell命令，q退出
>>cd
<paramiko.ChannelFile from <paramiko.Channel 1 (open) window=2097152 -> <paramiko.Transport at 0x6805cd00 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>>> <paramiko.ChannelFile from <paramiko.Channel 1 (open) window=2097152 -> <paramiko.Transport at 0x6805cd00 (cipher aes128-ctr, 128 bits) (active; 1 open channel(s))>>>                                                                                                                                    nnel(s))>>> <paramiko.ChannelFile

输入shell命令，q退出
>>q
(py38)
LuSai@LSX MINGW64 ~/51cto-task (master)
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py -S 111.229.5.166 -
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py -S 111.229.5.166
(py38) 
LuSai@LSX MINGW64 ~/51cto-task (master)
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py -S 111.229.5.166 -U readme.md readme1.md    
Namespace(download=False, filenames=['readme.md', 'readme1.md'], shell=None, ssh=['111.229.5.166'], upload=True)
<paramiko.client.SSHClient object at 0x0000016CB8C1CA90>
111.229.5.166 {'status': 0, 'msg': 'ok'}
(py38) 
LuSai@LSX MINGW64 ~/51cto-task (master)
$ C:/Users/LuSai/Anaconda3/envs/py38/python.exe c:/Users/LuSai/51cto-task/0405ssh_lishixiang/ssh_lishixiang.py -S 111.229.5.166 -D readme-back.md readme1. 
md
Namespace(download=True, filenames=['readme-back.md', 'readme1.md'], shell=None, ssh=['111.229.5.166'], upload=False)
<paramiko.client.SSHClient object at 0x0000019C7B40CA90>
111.229.5.166 {'status': 0, 'msg': 'ok'}
(py38) 
LuSai@LSX MINGW64 ~/51cto-task (master)
$
```

服务器端的ls -l操作
```shell
(base) [root@vm-lsx ~]# ls -l
total 44
-rw-r--r--  1 root root    72 Dec 27 23:20 1-test.ipynb
drwxr-xr-x  2 root root  4096 Dec 30 09:25 code
drwxr-xr-x 15 root root  4096 Dec 27 10:12 miniconda3
drwxr-xr-x  3 root root  4096 Dec 27 23:31 notebook
-rw-r--r--  1 root root    33 Jan 15 02:17 readme1.md  # 刚上传的文件
-rw-r--r--  1 root root 13129 Jan 10 16:36 ssh.log
drwxr-xr-x  3 root root  4096 Dec 27 09:33 test
-rw-r--r--  1 root root    38 Jan  9 21:55 test-new.txt
(base) [root@vm-lsx ~]# 
```