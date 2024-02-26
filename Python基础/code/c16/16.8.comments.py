import requests
comments=requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fynmzrs6000226&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&')
#print(comments.text)
#print('*'*50)
import json
jd=json.loads(comments.text.strip('var data='))  #转化成字典
print(jd)
print(jd['result']['count']['total'])
