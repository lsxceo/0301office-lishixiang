#!/usr/bin/env python
# -*- coding: utf-8 -*-
# admin.py


import argparse
from datetime import datetime
import minitoutiao as mt


class TouTiao:
    def __init__(self):
        self.parse = self.toutiao_parser()
        self.args = self.parse.parse_args()

    def toutiao_parser(self):
        """CLI工具"""
        parse = argparse.ArgumentParser(prog='MiniToutiao 功能列表')
        parse.add_argument('-S', '--show', action='store_true',
                           default='False', help='展示所有数据')
        parse.add_argument('-A', '--add', action='extend',
                           nargs=3, help='"文章名" "内容" "作者" 添加文章')
        parse.add_argument('-D', '--delete', help='"文章ID" 删除文章')
        # for key, value in d.items():
        #     print(f'{key} -> {value}')
        return parse

    def show_data(self):
        "显示全部数据"
        datas = {
            "status": 1,
            "statusText": "所有文章数据",
            "articles": []
        }
        articles = mt.session.query(mt.Article).all()
        if not articles:
            print(datas)
        else:
            data = []
            for article in articles:
                dic = {}
                author = mt.session.query(mt.Author).filter(
                    mt.Author.id == article.author_id).one()
                dic['id'] = article.id
                dic['author'] = author.name
                dic['title'] = article.title
                dic['content'] = article.content
                dic['create_date'] = article.create_date
                data.append(dic)
            datas['status'] = 0
            datas['articles'] = data
            print(datas)

    def add(self):
        "通过文章名，内容，作者增加文章"
        title, content, name = self.args.add
        authors = mt.session.query(mt.Author).filter(
            mt.Author.name == name).all()
        articles = mt.session.query(mt.Article).all()
        max_art_id = max(article.id for article in articles)
        if authors:
            author = authors[0]
            author_id = author.id
            author.article = mt.Article(
                id=max_art_id + 1, title=title, content=content, create_date=datetime.now().strftime('%Y-%m-%d'), author_id=author_id)
            mt.session.add(author.article)
            mt.session.commit()
            print('新文章添加成功！')
        else:
            authors = mt.session.query(mt.Author).all()
            max_id = max(author.id for author in authors)
            author_id = max_id + 1
            new_author = mt.Author(id=author_id, name=name)  # 添加新的作者
            new_article = mt.Article(id=max_art_id + 1, title=title, content=content,
                                     create_date=datetime.now().strftime('%Y-%m-%d'), author_id=author_id)  # 添加新的文章
            mt.session.add(new_author)
            mt.session.add(new_article)
            mt.session.commit()
            print(f'新文章添加成功，并更新了一位新作者"{name}"！')

        return name, title, content

    def delete(self):
        "通过文章ID删除文章"
        try:
            id = int(self.args.delete)
            status = mt.session.query(mt.Article).filter(
                mt.Article.id == id).delete()
            if status == 1:
                mt.session.commit()
                print(f'文章ID"{id}"已删除！')
            else:
                print(f'文章ID"{id}"不存在或者已被移除！')
        except Exception as e:
            print('出现错误，错误为：', e)


def main():
    """启动CLI工具的主要功能"""
    toutiao = TouTiao()
    args = toutiao.args
    if args.show is True:
        toutiao.show_data()
    if args.add:
        toutiao.add()
    if args.delete:
        toutiao.delete()
    if args.show is not True and args.add is None and args.delete is None:
        toutiao.parse.print_help()


if __name__ == "__main__":
    main()
