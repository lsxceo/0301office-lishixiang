#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# analysis.py
# 差评分析
# author: Lishixiang
"""有类，有日志，有数据结果"""

import csv
import re
import os
import logging
import jieba
import jieba.analyse


class Analyses:
    """文字段落分析工具"""
    def __init__(self, filename, stop_words_file):
        self.filename = filename
        self.stop_words_file = stop_words_file
        self.log = Log(os.getcwd(), 'analysis-log.log')
        self.log.output()
        self.logger = self.log.logger

    def get_all_text(self):
        """去除所有评价的句子"""
        comment_list = []
        with open(self.filename) as f:
            rows = csv.reader(f)
            for row in rows:
                # 筛选出符合条件的差评
                try:
                    if int(row[1]) >= 20 and row[2] == 'allstar20' or row[2] == 'allstar10' and len(row[-1]) > 10:
                        one_comment = row[-1]
                        comment_list.append(one_comment)
                except Exception:
                    pass
        self.logger.debug('找出所有有效的评价句子')
        return ''.join(comment_list)

    def cut_text(self, all_text):
        """找到评价中重要关键词"""
        jieba.analyse.set_stop_words(self.stop_words_file)
        text_tags = jieba.analyse.extract_tags(all_text, topK=30)
        self.logger.debug('找出评价中重要关键词')
        return text_tags

    def get_bad_words(self, text_tags, all_text):
        """根据关键词找到相应的句子"""
        words = {}
        for tag in text_tags:
            tag_re = re.compile(f'(\\w*{tag}\\w*)')
            # print(tag_re.findall(all_text))
            words[tag] = tag_re.findall(all_text)
        self.logger.info('根据关键词找到相应的句子')
        return words

    def analyse(self):
        all_text = self.get_all_text()
        text_tags = self.cut_text(all_text)
        # print(text_tags)
        words = self.get_bad_words(text_tags, all_text)
        with open('analysis.txt', 'w', encoding='utf-8') as f:
            for k, v in words.items():
                f.write(f"{k} '-->' {len(v)} {v}\n")
                print(k, '-->', len(v), v)
                f.write('-' * 50 + '\n')
                print('-' * 50)
        self.logger.warning('完成词条分析')


class Log:
    """日志类"""
    def __init__(self, log_path, log_file, formatter=None, log_name='analysis log', level=logging.DEBUG):
        if not formatter:
            self.formatter = self.set_formatter()
        self.path = os.path.join(log_path, log_file)
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(level)
        self.level = level

    def set_formatter(self):
        """设置formatter格式"""
        formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')
        return formatter

    def ch_log(self):
        """控制台的日志操作"""
        ch = logging.StreamHandler()
        ch.setLevel(self.level)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def fh_log(self):
        """文件的日志操作"""
        fh = logging.FileHandler(filename=self.path, encoding='utf-8')
        fh.setLevel(self.level)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

    def output(self, ch_enable=True, fh_enable=True):
        """输出日志文件"""
        if ch_enable:
            self.ch_log()
        if fh_enable:
            self.fh_log()


def main():
    analyses = Analyses('scaler-20.csv', 'stop_words.txt')
    analyses.analyse()


if __name__ == "__main__":
    main()
