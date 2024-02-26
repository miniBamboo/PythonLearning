#新浪新闻主页信息获取
import requests
from bs4 import BeautifulSoup
res =requests.get('https://news.sina.com.cn/') #china/
#'https://news.sina.com.cn/'
res.encoding='utf-8'
soup=BeautifulSoup(res.text, 'html.parser')
print(len(res.text))  #获取新浪新闻主页的全部信息

###仅提取新闻标题、来源的全部列表
for news in soup.select('#ad_entry_b2'): #.right-content
    alink=news.select('a')
    for link in alink:
        tl = link.text   
        a = link['href']
        print(tl,a)#打印标题和链接
        #print('-'*50)
"""for news in soup.select('.item'):#news-
    #print(news)
    #print('-'*50)
    '''if len(news.select('h2'))>0:  #这个判断是为了避免取出的有空值，注意冒号
    h2=news.select('h2')[0].text
    time=news.select('.time')[0].text  #因为time属性是class，显示所有时要加点“.time”
    a=news.select('a')[0]['href']
    print(time,h2,a)'''
    alink=news.select('a') 
    tl = alink[0].text   
    a = alink[0]['href']
    txt = news.select('.txt')[0].text
    print(tl,a,txt)
    print('-'*50)
    """
