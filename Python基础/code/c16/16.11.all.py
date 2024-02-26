# 获取当日新浪国内新闻的标题，内容，时间和评论数
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
import pandas

def getNewsdetial(newsurl):
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    #print(res.text)
    soup = BeautifulSoup(res.text,'html.parser')    
    newsTitle = soup.select('.main-title')[0].text.strip() #.main-title
    nt = datetime.strptime(soup.select('.date')[0].text.strip(),'%Y年%m月%d日 %H:%M')
    newsTime = datetime.strftime(nt,'%Y-%m-%d %H:%M')
    newsArticle = getnewsArticle(soup.select('.article p')) #.article p
    newsAuthor = soup.select('.source')[0].text.strip() #newsArticle[-1]
    return newsTitle,newsTime,newsArticle,newsAuthor
def getnewsArticle(news):
    newsArticle = []
    for p in news:
         newsArticle.append(p.text.strip())
    return newsArticle

# 获取评论数量
def getCommentCount(newsurl):
    m = re.search('doc-i(.+).shtml',newsurl)
    newsid = m.group(1)
    commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    comment = requests.get(commenturl.format(newsid))   #将要修改的地方换成大括号，并用format将newsid放入大括号的位置
    jd = json.loads(comment.text.lstrip('var data='))
    #print(jd['result']['status']['code'])
    count = -1 #评论异常
    if jd['result']['status']['code'] == 0:
        count = jd['result']['count']['total']
    #print(count)
    return count

def getNewsUrls():
#     得到新闻地址（即获得所有分页新闻地址）
    res =requests.get('https://news.sina.com.cn') #/china/
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text, 'html.parser')
    #print("新浪新闻(中国)主页的全部信息长度",len(res.text))  #获取新浪新闻主页的全部信息
    urls = []
    
    '''for div in soup.select('div'):
        for content in div.select('div'):
            "left-content-1 marBot"
            print(content)'''
    #i = 0
    for news in soup.select('.blk_09'): #right-content .left-content-1
        alink=news.select('a')
        #print(alink)
        for link in alink:
            link['href']
            oneUrl=str(link['href'])
            #print(link['href'])
            '''i += 1
            if i>2:
                break'''
            if(oneUrl.startswith('https://news')):
                urls.append(oneUrl)
                print(oneUrl)
            else:

                #print('pass')
                pass
    print('一共搜索到网址:',len(urls))
    return urls
# 取得新闻时间，编辑，内容，标题，评论数量并整合在total_2中
def getAllNews():
    title_all = []
    author_all = []
    commentCount_all = []
    article_all = []
    time_all = []
    #url_all = getNewsLinkUrl()
    print("第1步：获取所有新闻网址")
    url_all = getNewsUrls()
    print("第2步：获取新闻详细信息")
    for url in url_all:
        print(url)
        detial = getNewsdetial(url)
        #print(detial)
        title_all.append(detial[0])
        time_all.append(detial[1])
        article_all.append(detial[2])
        author_all.append(detial[3])
        commentCount_all.append(getCommentCount(url))
    print("第3步：新闻统计")
    total_2 = {'a_title':title_all,'b_article':article_all,'c_commentCount':commentCount_all,
               'd_time':time_all,'e_editor':author_all}
    return total_2

# ( 运行起始点 )用pandas模块处理数据并转化为excel文档
total_news = getAllNews()
print(total_news)
df = pandas.DataFrame(total_news)
print(df.head())
df.to_excel('news4.xls')
