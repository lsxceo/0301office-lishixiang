#!/usr/bin/env Python
# -*- coding=utf-8 -*-
# minitoutiao.py


from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


class Author(Base):
    """定义作者的对象"""
    __tablename__ = 'author'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), unique=True)
    city = Column('city', String(20))

    def __repr__(self):
        return self.name


class Article(Base):
    """定义文章的对象"""
    __tablename__ = 'article'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(20), unique=True, nullable=False)
    content = Column('content', String(180))
    comment = Column('comment', String(50))
    create_date = Column('create_date', Date)

    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author', back_populates='articles')

    def __repr__(self):
        return self.title


# 一对多关联
Author.articles = relationship(
    'Article', back_populates='author', order_by=Article.id)

engine = create_engine('mysql+pymysql://root:de8ug1234@localhost/de8ug')
Base.metadata.create_all(bind=engine)

DBsession = sessionmaker(bind=engine)
session = DBsession()


def add_author(session, id, name, city):
    """增加作者"""
    a = Author()
    a.id = id
    a.name = name
    a.city = city
    session.add(a)


def main():
    # add_author(session, 1, 'de8ug', 'Beijing')
    # add_author(session, 2, 'lsx', 'Taizhou')
    # add_author(session, 3, 'lee', 'Hangzhou')
    # session.commit()
    # s1 = session.query(Author).all()[0]
    # s1.articles = [
    #     Article(id=1, title='Python讲堂', content='学习python全栈课程',
    #             comment='还不错', create_date='2018-1-1'),
    #     Article(id=2, title='python爬虫', content='学习python爬虫',
    #             comment='讲到点了', create_date='2018-2-1')
    # ]
    # session.commit()
    # a4 = Author(id=4, name='she')
    # art3 = Article(id=103, title='new music', content='',
    #                comment='', create_date=datetime(2018, 10, 1))
    # session.add(a4)
    # session.add(art3)
    # session.commit()
    # print(s1)
    # print(session.query(Author).filter(Author.name == 'she').delete())
    # session.commit()

    # 查询
    # 根据作者查文章
    # print('All authors: ', session.query(Author).all())
    # print('create_time: ', session.query(Article).all()[0].create_date)
    # print('author by name: ', session.query(Author).filter(Author.name.startswith('d')).one())
    # print('author by name: ', session.query(Author).filter(Author.name.startswith('d')).first().articles)
    # print('author by id: ', session.query(Author).filter(Author.id > 1).all())
    # # 根据文章查作者
    # print('article by id: ', session.query(Article).filter(Article.id > 101).all())
    # print("get de8ug's article: ", session.query(Article).join(
    #     Article.author).filter(Author.name == 'de8ug').all())
    # 更新
    # article = session.query(Article).all()[0]
    # if hasattr(article.create_date, 'strftime'):
    #     strftime = getattr(article.create_date, 'strftime')
    # print('datetime to string: ', session.query(
    #     Article).update({Article.create_date: ''}))
    # session.commit()
    pass


if __name__ == "__main__":
    main()
