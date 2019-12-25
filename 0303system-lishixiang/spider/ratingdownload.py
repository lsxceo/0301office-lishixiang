#!usr/bin/env Python
# -*- coding=utf-8 -*-
# ratingdownload.py
# 豆瓣电影评论下载
# author：Lishixiang


import csv
import requests
import time
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from datetime import datetime
from urllib.parse import urlparse


class Throttle:
    """阀门类，控制下载速度，以免访问过快"""
    def __init__(self, delay=5):
        self.delay = delay  # 延迟时间
        self.domains = {}  # 用字典保存访问过的域名和时间

    def wait(self, url):
        """对访问过的域名添加延迟时间"""
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


class Downloader:
    """下载类，根据url返回内容"""
    def __init__(self, headers=None, num_retries=3, proxies=None, delay=5, timeout=30):
        self.headers = headers
        self.num_retries = num_retries
        self.proxies = proxies
        self.throttle = Throttle(delay)
        self.timeout = timeout

    def download(self, url):
        print('下载页面：', url)
        self.throttle.wait(url)
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=self.timeout)
            print(response.status_code)
            if response.status_code == 200:
                return response.content
            return None
        except RequestException as e:
            print('error', e.response)
            html = ''
            if hasattr(e.response, 'status_code'):
                code = e.response.status_code
                print('error code', code)
                if self.num_retries > 0 and 500 <= code < 600:
                    html = self.download(url)
                    self.num_retries -= 1
            else:
                code = None
        return html


class ItemSpider:
    """抓取评价信息"""
    def __init__(self, headers=None, num_retries=3, proxies=None, delay=5, timeout=30):
        # self.headers = headers
        # self.num_retries = num_retries
        # self.proxies = proxies
        # self.throttle = Throttle(delay)
        # self.timeout = timeout
        self.download = Downloader(headers, num_retries, proxies, delay, timeout)

    def get_comment(self, url):
        """下载页面，找出有用的标签"""
        page = self.download.download(url)
        soup = BeautifulSoup(page, 'lxml')
        comments = soup.find_all('div', attrs={'class': 'comment-item'})
        return comments

    def find_all(self, comments):
        """找出所有评价"""
        data_list = []
        for comment in comments:
            name = comment.find('div', attrs={'class': 'avatar'}).find('a')['title'].encode('GBK', 'ignore').decode('GB18030')
            print('name: ', name)
            votes = comment.find('span', attrs={'class': 'votes'}).text
            print('votes: ', votes)
            rating_level = comment.find('span', attrs={'class': re.compile(r'.*?'), 'title': re.compile(r'.*?')})['class'][0]
            print('rating_level: ', rating_level)
            rating_text = comment.find('span', attrs={'class': re.compile(r'(.*?)'), 'title': re.compile(r'(.*?)')})['title']
            print('rating_text: ', rating_text)
            comment_time = comment.find('span', attrs={'class': 'comment-time'})['title']
            print('comment_time: ', comment_time)
            short = comment.find('span', attrs={'class': 'short'}).text.encode('GBK', 'ignore').decode('GB18030')
            print('short: ', short)
            row = []
            row.append(name)
            row.append(votes)
            row.append(rating_level)
            row.append(rating_text)
            row.append(comment_time)
            row.append(short)
            data_list.append(row)
        return data_list

    def fetch_data(self, url, start_page, end_page, page_offset, filename, callback=None):
        # all_list = self.find_all(self.get_comment(url))
        all_list = []
        for page in range(start_page, end_page*page_offset, page_offset):
            data_list = self.find_all((self.get_comment(url.format(page))))
            print(f'第{page // page_offset + 1}页下载完成')
            print('-' * 50)
            all_list += data_list

        if callback:
            callback(filename, ('昵称', '支持票数', '评价星级', '评价等级', '时间', '评价内容'), all_list)


class Recorder:
    """记录类，根据不同保存类型使用相应方法。通过类对象使用回调函数方法直接调用"""
    def __init__(self, save_type='csv'):
        self.save_type = save_type

    def __call__(self, filename, fields, all_list):
        if hasattr(self, self.save_type):
            func = getattr(self, self.save_type)
            return func(filename, fields, all_list)
        else:
            return {'status': 1, 'statusText': 'no record function'}

    def csv(self, filename, fields, all_list):
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(fields)
                for row in all_list:
                    writer.writerow(row)
            return {'status': 0, 'statusText': 'csv saved'}
        except Exception as e:
            print(e)
            return {'status': 1, 'statusText': 'csv error'}


def main():
    url = 'https://movie.douban.com/subject/30413052/comments?start={}&limit=20&sort=new_score&status=P'
    headers = {
        'Referer': 'https://movie.douban.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    }
    spider = ItemSpider(headers=headers)
    spider.fetch_data(url, 0, 10, 20, 'scaler-20.csv', Recorder('csv'))


if __name__ == "__main__":
    main()
