#!/usr/bin/env python
# -*- coding: utf-8 -*-
# admin.py


import argparse
from datetime import datetime
import minitoutiao as mt


def toutiao_parser():
    """CLI工具"""
    parse = argparse.ArgumentParser(prog='MiniToutiao 功能列表')
    parse.add_argument('-S', '--show', action='store_true',
                       default='False', help='展示所有数据')
    parse.add_argument('-A', '--add', action='extend',
                       nargs=3, help='"文章名" "内容" "作者" 添加文章')
    parse.add_argument('-D', '--delete', help='"文章ID" 删除文章')
    # print(parse.print_help())
    # args = parse.parse_args()
    # d = args.__dict__
    # for key, value in d.items():
    #     print(f'{key} -> {value}')
    return parse


def main():
    """启动CLI工具的主要功能"""
    parse = toutiao_parser()
    args = parse.parse_args()
    if args.show is True:
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

    if args.add:
        title, content, name = args.add
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

    if args.delete:
        try:
            id = int(args.delete)
            status = mt.session.query(mt.Article).filter(
                mt.Article.id == id).delete()
            if status == 1:
                mt.session.commit()
                print(f'文章ID"{id}"已删除！')
            else:
                print(f'文章ID"{id}"不存在或者已被移除！')
        except Exception as e:
            print('出现错误，错误为：', e)

    if args.show is not True and args.add is None and args.delete is None:
        parse.print_help()


if __name__ == "__main__":
    main()
