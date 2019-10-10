#!/usr/bin/env python
# -*- coding:utf-8 -*-
# configadmin.py
# author: lishixiang


import configparser
from configparser import ExtendedInterpolation
import os
from . import setting


class ConfigAdmin():
    "配置文件的类"

    def __init__(self, config_path, config_name):
        "初始化"
        settings = setting.Settings()
        self.data = settings.data
        self.config = configparser.ConfigParser(interpolation=ExtendedInterpolation())
        self.config_path = config_path
        self.config_name = config_name
        self.path = os.path.join(self.config_path, self.config_name)
        if not os.path.exists(self.path):
            self.write_config(settings.data)
        self.config.read(self.path)

    def write_config(self, data: dict):
        "写配置"
        ret = {'status': 0, 'statusText': 'ok!'}
        for k, v in data.items():
            self.config[k] = v
        with open(self.path, 'w') as f:
            self.config.write(f)
        return ret

    def read_config(self, section, option):
        "读配置"
        config_dic = {}
        try:
            self.config.read(self.path)
            config_data = self.config[section][option]
            return config_data
        except Exception as e:
            config_dic['error'] = e
            return config_dic

    def add_config(self, section, option, value):
        "添加配置"
        ret = {'status': 0, 'statusText': 'ok!'}
        try:
            self.config.read(self.path)
            if self.config.has_section(section):
                self.config.set(section, option, value)
            else:
                self.config.add_section(section)
                self.config.set(section, option, value)
            with open(self.path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            ret['status'] = 1
            ret['statusText'] = e
        return ret

    def check_config(self):
        "检查配置: 把配置文件格式化打印出来"  
        self.config.read(self.path)
        for section in self.config.sections():
            print(f"[{section}]")
            for option in self.config.options(section):
                print(f'{option} = {self.config[section][option]}')


def main():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    config_path = os.path.join(base_dir, 'conf')
    config = ConfigAdmin(config_path, 'admin.ini')
#     print(config.write_config(data))
#     print(config.read_config('debug', 'db_type'))
#     print(config.add_config('lsx', 'db_path', '${base_dir}/lsx.pkl'))
#     print(config.add_config('lsx', 'db_type', 'pkl'))
    config.check_config()

if __name__ == '__main__':
    main()