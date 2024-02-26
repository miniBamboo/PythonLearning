#获取某一篇文章的标题、日期、来源、正文等内容
import requests
from bs4 import BeautifulSoup
res =requests.get('http://news.sina.com.cn/o/2018-03-16/doc-ifysiesm9100707.shtml')
res.encoding='utf-8'
#print(res.text)  #这里得到的是带有html标签的网页内容
soup=BeautifulSoup(res.text, 'html.parser')  #将requests.get获取得到的res对象变成BeautifulSoup对象，供后面的每个字段属性的提取

title=soup.select('.main-title')[0].text #获取标题 
datesource=soup.select('.date')[0].text  #获取日期
source=soup.select('.source')[0].text  #获取来源
sourcelink=soup.select('.source')[0]['href']  #获取来源链接
article=soup.select('.article')[0].text  #获取正文内容
print(title)
print(datesource)
print(source)
print(sourcelink)
print(article)
