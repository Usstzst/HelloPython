'''    API   '''
# 显示维基百科英文版的编辑者所在位置的可视图

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json
from urllib.error import HTTPError

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIps(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")

    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is:"+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    ipAddresses  = bsObj.findAll("a",{"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while (len(links)>0):
    for link in links:
        print('---------------')
        historyIps = getHistoryIps(link.attrs['href'])
        for historyIP in historyIps:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + "is from " +country)


    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)
