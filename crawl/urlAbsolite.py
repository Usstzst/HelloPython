'''  

对 URL 链接进行清理和标准化  

'''

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getAbsoliteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" +source[4:]
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url
