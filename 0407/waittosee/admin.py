#!usr/bin/env Python
# -*- coding: utf-8 -*-
# admin.py


import json
import os
from datetime import datetime
import argparse
import paramiko


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "111.229.5.166"
USER = "root"
KEY_FILENAME = r"C:\Users\LuSai\.ssh\yun_rsa"


paramiko.util.log_to_file("lsx-ssh.log")
parser = argparse.ArgumentParser("LSX ssh 功能列表。。。")


class AcceptPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


class MySSH:
    """SSH"""

    def __init__(self):
        self.client = self.connect()

    def close(self):
        self.client.close()

    def connect(self):
        """连接服务器"""
        client = ''
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(AcceptPolicy())
            client.connect(HOST, username=USER, key_filename=KEY_FILENAME)
        except Exception as e:
            print(e)
        return client

    def download_file(self,
                      remote_file_path='code/proj/data.json',
                      local_file_path=os.path.join(BASE_DIR, 'data.json')):
        """从服务器下载文件"""
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


class Data_Query:
    """查询中英文鸡汤"""

    def __init__(self):
        date_ = input('请输入要查询日期（示例2010-5-10）：')
        self.query_date = self.date_query(date_)

    def date_query(self, date_):
        """把输入的内容格式化"""
        try:
            query_date = datetime.strptime(date_, '%Y-%m-%d').date()
            return query_date
        except Exception as e:
            print(e)
        return None

    def query(self):
        """通过日期查询内容，并格式化输出"""
        if self.query_date is None:
            print('日期输入有误！')
        else:
            try:
                with open(os.path.join(BASE_DIR, 'data.json'), 'r') as f:
                    data = json.load(f)
                soup_data = data['dailysentence']
                for d in soup_data:
                    if datetime.strptime(d['id'], '%Y-%m-%d %X').date() == self.query_date:
                        print(d['en'], '\n', d['cn'], '\n')
            except Exception as e:
                print(e)


def main():
    parser.add_argument('-D', '--download', dest="download",
                        action="store_true", help="下载文件")
    args = parser.parse_args()
    if not args.download:
        parser.print_help()
        return
    else:
        client = MySSH()
        if client:
            stdout = client.download_file()
            print(stdout)
        client.close()
    data_query = Data_Query()
    data_query.query()


if __name__ == "__main__":
    main()
