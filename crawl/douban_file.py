import urllib.request
import socket
import re
import sys
import os

# 爬取豆瓣整个网页并下载

def saveFile(data):
    save_path = r"F:\new\temp.out"
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()

weburl = 'http://www.douban.com/'
webheader1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

webheader2 = {
    'Connection': 'Keep-Alive',
    'Accept': 'text.html, application/xhtml+xml, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Host': 'www.douban.com',
    'DNT': '1'

}

req = urllib.request.Request(url=weburl, headers=webheader2)
webPage = urllib.request.urlopen(req)
data = webPage.read()
saveFile(data)
data = data.decode('UTF-8')
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())