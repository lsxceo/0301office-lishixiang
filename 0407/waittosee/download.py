#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# download.py
# TODO


import time
from datetime import datetime
from urllib.parse import urlparse
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


class Throttle:
    """阀门类，对相同域名的访问添加延迟时间，避免访问过快"""

    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_seconds = self.delay - \
                (datetime.now() - last_accessed).seconds
            if sleep_seconds > 0:
                time.sleep(sleep_seconds)
        self.domains[domain] = datetime.now()


class Downloader:
    """下载类，根据url返回内容"""

    def __init__(self, headers=None, num_retries=3, proxies=None, delay=2, timeout=30):
        self.headers = headers
        self.num_retries = num_retries
        self.proxies = proxies
        self.timeout = timeout
        self.throttle = Throttle(delay)

    def download(self, url, is_json=False):
        print('下载页面：', url)
        self.throttle.wait(url)
        try:
            response = requests.get(
                url, headers=self.headers, proxies=self.proxies, timeout=self.timeout)
            print(response.status_code)
            if response.status_code == 200:
                return response.content
            return None
        except RequestException as e:
            print('error: ', e.response)
            html = ''
            if hasattr(e.response, 'status_code'):
                code = e.response.status_code
                print('error code: ', code)
                if self.num_retries > 0 and 500 <= code < 600:
                    html = self.download(url)
                    self.num_retries -= 1
            else:
                code = None
        return html


class ContentSpider:
    """抓取英文语句的信息"""

    def __init__(self, headers=None, num_retries=3, proxies=None, delay=2, timeout=30):
        self.headers = headers
        self.num_retries = num_retries
        self.proxies = proxies
        self.throttle = Throttle(delay)
        self.timeout = timeout
        self.download = Downloader(
            headers, num_retries, proxies, delay, timeout)

    def get_data(self, url):
        data = self.download.download(url)
        soup = BeautifulSoup(data, 'lxml')
        # print(soup)
        english = soup.find('div', attrs={'class': 'detail-content-en'}).text
        chinese = soup.find('div', attrs={'class': 'detail-content-zh'}).text
        dic = {}
        dic['english'] = english
        dic['chinese'] = chinese
        return dic


def main():
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }
    url = "http://news.iciba.com/views/dailysentence/daily.html#!/detail/title/2020-05-09"
    spider = ContentSpider(headers=headers)
    print(spider.get_data(url))


if __name__ == "__main__":
    main()
