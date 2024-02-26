#requests.get示例
import requests
res=requests.get('http://news.sina.com.cn/china/')  
res.encoding='utf-8'  #这一句是为了避免中文乱码
print(res)   #输出结果是<Response [200]>，可知resquests.get返回回复的数量，而不是回复的内容
print(res.text)  #因此加上“.text”才是得到网页内容
