#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# ssh_lishixiang.py


import os
import argparse
import paramiko

from config import ConfigAdmin
base_dir = os.path.abspath(os.path.dirname(__file__))
paramiko.util.log_to_file("lsx-ssh.log")  # 输出日志


class AcceptPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


class Lsx_Parser_SSH:
    """一个服务器管理CLI工具"""

    def __init__(self):
        self.parser = self.sshparser()
        self.client = ''

    def sshparser(self):
        parser = argparse.ArgumentParser(prog='LSX SSH功能列表')
        parser.add_argument('-S', '--ssh', nargs='*', help='用密钥的方式登录服务器')
        parser.add_argument('-U', '--upload', dest='upload',
                            action='store_true', help='上传文件，需要追加文件名')
        parser.add_argument('-D', '--download', dest='download',
                            action='store_true', help='下载文件，需要追加文件名')
        parser.add_argument(dest='filenames',
                            nargs='*',
                            help='文件列表，第一个表示本地文件，第二个表示远程文件')
        parser.add_argument('-C', '--shell', dest='shell', default=None,
                            action='store_true', help='进入交互控制台，需要先-S登录服务器')
        return parser

    def connect(self, host, user, key_filename):
        """连接服务器"""
        client = ''
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(AcceptPolicy())
            client.connect(host, username=user, key_filename=key_filename)
            print(client)
        except Exception as e:
            print(e)
        self.client = client
        return client

    def send_cmd(self, cmd):
        """发送命令，取得返回值"""
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            print(stdout, stderr)
            return stdout
        except paramiko.SSHException as e:
            print(e)

    def upload_file(self, local_file_path, remote_file_path):
        """put local file to remote"""
        ret = {"status": 0, "msg": "ok"}
        try:
            if self.client:
                ftp_client = self.client.open_sftp()
                ftp_client.put(local_file_path, remote_file_path)
                ftp_client.close()
            else:
                ret["status"] = 1
                ret["msg"] = "error"
        except Exception as e:
            print(e)
            ret["status"] = 2
            ret["msg"] = e
        return ret

    def download_file(self, remote_file_path, local_file_path):
        """get file from remote server"""
        ret = {"status": 0, "msg": "ok"}
        try:
            if self.client:
                ftp_client = self.client.open_sftp()
                ftp_client.get(remote_file_path, local_file_path)
                ftp_client.close()
            else:
                ret["status"] = 1
                ret["msg"] = "error"
        except Exception as e:
            print(e)
            ret["status"] = 2
            ret["msg"] = e
        return ret

    def close(self):
        self.client.close()


def main():
    lsx_parser_ssh = Lsx_Parser_SSH()
    args = lsx_parser_ssh.parser.parse_args()
    print(args)
    if args.ssh:
        for ssh in args.ssh:
            config = ConfigAdmin(base_dir, 'config.ini')
            ret = config.read_config(ssh, 'user')
            if ret:
                user = config.read_config(ssh, 'user')
                key_filename = config.read_config(ssh, 'key_file')
                # print(user, key_filename)
                if args.filenames:
                    client = lsx_parser_ssh.connect(ssh, user, key_filename)
                    if args.upload:
                        local_file_path = args.filenames[0]
                        remote_file_path = args.filenames[1]
                        stdout = lsx_parser_ssh.upload_file(
                            local_file_path, remote_file_path)
                        print(ssh, stdout)
                    elif args.download:
                        local_file_path = args.filenames[0]
                        remote_file_path = args.filenames[1]
                        stdout = lsx_parser_ssh.download_file(
                            remote_file_path, local_file_path)
                        print(ssh, stdout)
                    else:
                        lsx_parser_ssh.parser.print_help()
                    lsx_parser_ssh.close()
                elif args.shell:
                    client = lsx_parser_ssh.connect(ssh, user, key_filename)
                    if client:
                        while True:
                            print('输入shell命令，q退出')
                            cmd = input(">>")
                            if cmd == 'q':
                                break
                            stdout = lsx_parser_ssh.send_cmd(cmd)
                            print(stdout.read().decode())
                        lsx_parser_ssh.close()

    else:
        lsx_parser_ssh.parser.print_help()


if __name__ == '__main__':
    main()
