import urllib.request


url='http://www.whatismyip.com.tw/'
proxy_support=urllib.request.ProxyHandler({'http':'211.138.121.38:80'})

opener=urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)




