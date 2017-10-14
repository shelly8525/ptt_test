#!/usr/bin/env python
#coding=utf-8

from urlparse import urljoin
import requests
import urlparse
from bs4 import BeautifulSoup

from utils import pretty_print

import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
i=0

INDEX = 'https://www.ptt.cc/bbs/movie/index.html'
NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a


def get_posts_on_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    articles = soup.find_all('div', 'r-ent')

    posts = list()
    for article in articles:
        meta = article.find('div', 'title').find('a') or NOT_EXIST
        posts.append({
            'title': meta.getText().strip(),
            'link': meta.get('href'),
            'push': article.find('div', 'nrec').getText(),
            'date': article.find('div', 'date').getText(),
            'author': article.find('div', 'author').getText(),
        })

    next_link = soup.find('div', 'btn-group-paging').find_all('a', 'btn')[1].get('href')

    return posts, next_link


def get_pages(num):
    page_url = INDEX
    all_posts = list()
    for i in range(num):
        posts, link = get_posts_on_page(page_url)
        all_posts += posts
        page_url = urljoin(INDEX, link)
    return all_posts


if __name__ == '__main__':
    pages = 200
    for post in get_pages(pages):
        i+=1
	pretty_print(post['push'], post['title'], post['date'], post['author'])
	c.execute("INSERT INTO COMPANY1 (id,PUSH,TITLE,DATE,NAME) VALUES(?,?,?,?,?)",(i,post['push'], post['title'], post['date'], post['author']))
        conn.commit()
