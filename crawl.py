# -*- coding: utf-8 -*
'''爬取律师函页面信息'''

from bs4 import BeautifulSoup
import requests
from bs4 import Tag
import pymongo

import requests
import json
import os
from pymongo import MongoClient
import time
from ast import literal_eval
import re
import pprint



client = MongoClient('localhost', 27017)

db = client.test_database
posts = db.posts


# 爬取详情url
def getDetailUrl(url):

    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    info = soup.find('table', {'class': 'tbl_cqhmd'})
    detailUrl = info.find('a').get('href')

    return detailUrl

import jieba

# 从详情URL获取
def get_data(detailUrl):

    data = requests.get(detailUrl)
    soup = BeautifulSoup(data.text, 'html.parser')
    arr = soup.findAll('div', {'class':'personal'})

    for i in arr[0].ul:
        # print (type(i))
        if isinstance(i, Tag):
            span = i.find('span')
            if not isinstance(span, int): # & span is not None:
                if span.text.find(("—")) == -1:
                    m = span.text.strip()


                    #print(span.text.strip())
                    # print ("result", result)
                    ch = "：".encode('utf-8').decode('utf-8')

                    key, value = m.split(ch, 1)[0], m.split(ch, 1)[-1]
                    print(key, value)



                posts.insert_one({key: value})



# 爬取律师函账户信息
for i in range(1):
    i = i+1
    url = 'http://www.cuitx.cn/Dbln/Noticect.aspx?Pageindex='+str(i)
    detail = getDetailUrl(url)
    get_data(detail)


# print("")
# pprint.pprint(posts.find_one())
















