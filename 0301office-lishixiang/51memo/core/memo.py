#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo.py
# author: lishixiang

"""
1.添加Memo类，至少包含id，name，thing，date四个属性，date可以暂时使用字符串表示，比如‘1.2’，‘3.8’，暂时不用考虑时间相关模块

2.id属性为只读，其他属性可读写

3.添加MemoAdmin类，作为主体程序，管理Memo类构成的列表，进行Memo的增删改查（相应方法为add, del, modify, query），处理输入输出。

4.所有Memo记录使用pickle进行读写，数据文件为db.pkl, 读写方法为save和load

5.各个类中的每个方法必须添加说明doc-string（即def下一行加一句注释），每个类必须添加注释说明，解释作用(缺一条减10分)
"""

import pickle
import time


class Memo:
    """备忘事项的类"""
    def __init__(self, date, frame, hour, minute, thing, name):
        "初始化并设置属性"
        self._id = 0
        self.date = date
        self.frame = frame
        self.hour = hour
        self.minute = minute
        self.thing = thing
        self.name = name
        # self.dic = self.memo_dict()
        
    def memo_dict(self):
        "把各个属性存到字典中"
        dic = {
            'id': self._id,
            'date': self.date,
            'frame': self.frame,
            'hour': self.hour,
            'minute': self.minute,
            'thing': self.thing,
            'name': self.name
        }
        return dic

    @property  # 设置私有属性
    def id(self):
        return self._id

    @id.setter  # 对私有属性的值进行操作
    def id_set(self, value):
        self._id = value

    def __str__(self):  # 设置str()函数
        minute = str(self.minute).rjust(2, '0')
        name = '@'.join(self.name)
        return f'{self.date}:{self.frame} {self.hour}:{minute}{self.thing}@{name}'
