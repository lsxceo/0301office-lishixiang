#!/usr/bin/env python
# -*- coding:utf-8 -*-


import configparser
import os
base_dir = os.path.abspath(os.path.dirname(__file__))
data = {
    'DEFAULT': {
        'base_dir': base_dir,
        'user': 'root',
        'key_file': "C:/Users/LuSai/.ssh"
    }
}


class ConfigAdmin():
    "配置文件的类"

    def __init__(self, base_dir, config_name, data=data):
        self.path = os.path.join(base_dir, config_name)
        self.config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation())
        if not os.path.exists(self.path):
            self.write_config(data)

    def write_config(self, data: dict):
        "写配置"
        config_dic = {'status': 0, 'statusText': 'done'}
        try:
            for k, v in data.items():
                self.config[k] = v
            with open(self.path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            config_dic['status'] = 1
            config_dic['statusText'] = e
        return config_dic

    def read_config(self, section, option):
        "读配置"
        config_dic = {'status': 0, 'statusText': 'done'}
        try:
            self.config.read(self.path)
            config_data = self.config[section][option]
            return config_data
        except Exception as e:
            config_dic['status'] = 1
            config_dic['statusText'] = e
            return config_dic

    def add_config(self, section, option, value):
        "添加配置"
        config_dic = {'status': 0, 'statusText': 'done'}
        try:
            self.config.read(self.path)
            if section in self.config:
                config_dic['status'] = 1
                config_dic['statusText'] = 'section is exist'
            else:
                self.config.add_section(section)
                self.config.set(section, option, value)
                with open(self.path, 'w') as f:
                    self.config.write(f)
        except Exception as e:
            config_dic['status'] = 1
            config_dic['statusText'] = e
        return config_dic

    def check_config(self, section, option, value):
        "检查配置"
        config_dic = config_dic = {'status': 0, 'statusText': 'done'}
        try:
            self.config.read(self.path)
            if section not in self.config:
                self.config.add_section(section)
            self.config.set(section, option, value)
            with open(self.path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            config_dic['status'] = 1
            config_dic['statusText'] = e
        return config_dic


def main():
    config = ConfigAdmin(base_dir, 'config.ini')
    add = config.add_config('111.229.5.166', 'key_file',
                            '${DEFAULT:key_file}/yun_rsa')
    print(add)
    read = config.read_config('111.229.5.166', 'key_file')
    print(read)


if __name__ == '__main__':
    main()
