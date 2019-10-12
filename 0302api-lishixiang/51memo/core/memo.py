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

from .create_event import Create_event


class Memo:
    """备忘事项的类"""
    def __init__(self, event='', id_='', time_='', thing='', name=''):
        "初始化并设置属性"
        self.event = event
        self.id_ = id_
        self.time_ = time_
        self.thing = thing
        self.name = name
        if self.event != '':
            self.event = Create_event(event)
            self.event_format_list = self.event.new_list
            self._id = 0
            self.time_ = self.event_format_list[0]
            self.thing = self.event_format_list[1]
            self.name = self.event_format_list[2]

    def memo_dict(self):
        "把各个属性添加到字典中"
        dic = {
            'id': self._id,
            'time_': self.time_,
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
        if len(self.name) == 1:
            at_people = '@' + self.name[0]
        else:
            at_people = '@' + '@'.join(self.name)
        if self.event == '' and self.id_ != '':
            return f'ID: {self.id_}    {self.time_} {self.thing} {at_people}'
        elif self.id_ == '' and self.event == '':
            return f'{self.time_} {self.thing}{at_people}'
        else:
            return f'{self.time_} {self.thing}{at_people}'


def main():
    # event = '下个月5号下午6点吃火锅@小李@小周@小王'
    # memo = Memo(event)
    mm = Memo(id_=1, time_='2019.11.11', thing='吃火锅', name=['我'])
    print(mm)


if __name__ == "__main__":
    main()
