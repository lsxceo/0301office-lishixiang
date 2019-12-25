#!/usr/bin/env Python
# -*- coding=utf-8 -*-


import re
import os
import requests
import time
from urllib.parse import urlparse
from datetime import datetime
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


base_dir = r'C:\Users\LuSai\Pictures\python download'
os.chdir(base_dir)
headers = {
        'Referer': 'https://www.meitulu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    }


class Throttle:
    """阀门类，对相同域名的访问添加延迟时间，避免访问过快"""
    def __init__(self, delay):
        # 延迟时间，避免访问过快
        self.delay = delay
        # 用字典保存访问某域名的时间
        self.domains = {}

    def wait(self, url):
        """对访问过的域名添加延迟时间"""
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()


class MtlDownload:
    """mtl爬虫测试"""
    def __init__(self, headers=headers, proxies=None, delay=2):
        self.headers = headers
        self.proxies = proxies
        self.throttle = Throttle(delay)

    def download(self, url, headers=headers, num_retries=3):
        """网页下载"""
        print('Downloading:', url)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.content
            return None
        except RequestException as e:
            print('error:', e.response)
            html = ''
            if hasattr(e.response, 'status_code'):
                code = e.response.status_code
                print('error code:', code)
                if num_retries > 0 and 500 <= code < 600:
                    html = self.download(url, headers, num_retries-1)
            else:
                code = None
        return html

    def picture_download(self, url, dirname, pic_name, headers=headers, num_retries=3):
        "下载图片"
        self.throttle.wait(url)
        print('下载图片：', url, dirname, pic_name)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                with open(os.path.join(base_dir, dirname, pic_name + '.jpg'), 'wb') as f:
                    f.write(response.content)

        except RequestException as e:
            print('error:', e.response)
            if hasattr(e.response, 'status_code'):
                code = e.response.status_code
                print('error code:', code)
                if num_retries > 0 and 500 <= code < 600:
                    self.picture_download(url, dirname, pic_name, headers, num_retries-1)
                else:
                    print(pic_name, '下载失败！')

    def find_picture(self, content, headers=headers):
        # 找出名字，图片网址，图片数量
        name = re.findall(r'模特：(.*?)\n', content.text)[0]
        name = re.sub('模特：', '', name).strip()
        print('name', name)
        # print(soup.find('p'))
        num = re.search(r'\d+', content.find('p').text).group()
        print('num', num)
        id = re.search(r'\d+', content.find('a')['href']).group()
        print('id', id)
        # 如果目录不存在就创建目录，并计算目录里的文件数量
        if not os.path.isdir(name):
            os.mkdir(name)
        pic_num = len(os.listdir(name))
        # url = 'https://mtl.xtpxw.com/images/img/{}/{}.jpg'
        url = 'https://mtl.gzhuibei.com/images/img/{}/{}.jpg'
        for i in range(1, int(num) + 1):
            self.picture_download(url.format(id, str(i)), name, str(i + pic_num), headers=headers)

    def find_picturl_by_url(self, url, headers=headers):
        # 找出名字，图片网址，图片数量
        html = self.download(url, headers=headers)
        soup = BeautifulSoup(html, 'lxml')
        name = re.findall(r'模特姓名：(.*?)\n', soup.find('div', attrs={'class': 'width'}).text)[0]
        name = re.sub('模特姓名：', '', name).strip()
        print('name:', name)
        num_content = re.search(r'图片数量(.*?)\n', soup.find('div', attrs={'class': 'width'}).text).group()
        num = re.search(r'\d+', num_content).group()
        print('num:', num)
        id = re.search(r'\d+', url).group()
        print('id:', id)
        # 创建目录
        if not os.path.isdir(name):
            os.mkdir(name)
        pic_num = len(os.listdir(name))
        print('pic_num:', pic_num)
        url = 'https://mtl.gzhuibei.com/images/img/{}/{}.jpg'
        for i in range(1, int(num) + 1):
            self.picture_download(url.format(id, str(i)), name, str(i + pic_num), headers=headers)

    def find_all(self, name, headers=headers):
        search_url = 'https://www.meitulu.com/search/{}'.format(name)
        html = self.download(search_url, headers=headers)
        soup = BeautifulSoup(html, 'lxml')
        url_content_list = soup.find('ul', attrs={'class': 'img'}).find_all('li')
        url_list = []
        for url_content in url_content_list:
            url = url_content.find('a')['href']
            url_list.append(url)
        for url in url_list:
            self.find_picturl_by_url(url, headers=headers)


def main():
    # url = 'https://www.meitulu.com/item/2621.html'
    name = '宁宁'
    mtldownload = MtlDownload()
    # mtldownload.find_picturl_by_url(url, headers=headers)
    mtldownload.find_all(name)


if __name__ == "__main__":
    main()
