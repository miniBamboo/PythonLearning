#获取网页id
newsurl='https://news.sina.com.cn/c/2019-05-06/doc-ihvhiqax6993505.shtml'
newsurl0='http://news.sina.com.cn/gov/2017-11-02/doc-ifynmzrs6000226.shtml'
newsid=newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
print(newsid)

#获取网页id（正则表达式法）
import re
m=re.search('doc-i(.+).shtml',newsurl)
print(m) #查看匹配结果，match部分是匹配到的部分
print(m.group(0)) #匹配到的部分
print(m.group(1)) #匹配到的“(.+)”部分
