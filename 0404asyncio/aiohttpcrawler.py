#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# aiohttpcrawler.py
# author: lishixiang


import json
import logging
import sys
import asyncio
import aiohttp
from bs4 import BeautifulSoup


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-10s: %(message)s'
)


class AiohttpCrawler:
    """异步爬取网站的所有链接"""
    def __init__(self, url=''):
        self.url = url
        self.results = {}
        if len(sys.argv) > 1:
            if sys.argv[1] == '-help':
                print('功能帮助：')
                print('在终端通过输入命令行参数的方式直接运行：示例(python aiohttpcrawler.py <url>)')
                exit()
            self.url = sys.argv[1]

    async def get_content(self):
        """用异步方式下载网页内容返回soup"""
        logging.debug('load html...')
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                html = await resp.text()
                if html:
                    soup = BeautifulSoup(html, 'lxml')
                    title = soup.find('title').get_text()
                    if title:
                        self.results['title'] = title
                    return soup

    def get_tag_list(self, soup):
        """找出所有标签"""
        logging.debug('get tag list...')
        tag_list = []
        for tag in soup.find_all(True):
            tag_list.append(tag.name)
        tag_list = list(set(tag_list))
        return tag_list

    def get_value_list(self, tag_list, soup):
        """通过标签名字找出所有的标签"""
        logging.debug('get value soup...')
        value_list = []
        for tagname in tag_list:
            value_soups = soup.find_all(tagname)
            for value_soup in value_soups:
                dic = value_soup.attrs
                for url in dic.values():
                    value_list.append(url)
        return value_list

    def get_url_list(self, value_list):
        """通过标签找出所有的链接地址"""
        logging.debug('get url list...')
        url_list = []
        for v in value_list:
            if type(v) == str:
                if v[0:4] == 'http':
                    url_list.append(v)
                if v[:1] == '/':
                    url = self.url.strip('/') + v
                    url_list.append(url)
        url_list = list(set(url_list))
        return url_list

    def save_file(self, name):
        logging.debug('saving file...')
        with open(name + '-urls' + '.json', 'w') as f:
            json.dump(self.results, f)

    def run(self):
        try:
            soup = asyncio.run(self.get_content())
            tag_list = self.get_tag_list(soup)
            value_list = self.get_value_list(tag_list, soup)
            url_list = self.get_url_list(value_list)
            self.results['url'] = self.url
            self.results['url_addr'] = url_list
            name = self.url.split('//')[1].split('/')[0].strip('www.').split('.')[0]
            self.save_file(name)
        except Exception as e:
            print('出现错误，错误为:', e)


def main():
    crawler = AiohttpCrawler()
    crawler.run()


if __name__ == "__main__":
    main()
