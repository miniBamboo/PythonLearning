import requests
from bs4 import BeautifulSoup
res =requests.get('http://news.sina.com.cn/gov/2017-11-02/doc-ifynmzrs6000226.shtml')
res.encoding='utf-8'

soup=BeautifulSoup(res.text, 'html.parser') 
title=soup.select('#artibody')[0].text 

print(title)
