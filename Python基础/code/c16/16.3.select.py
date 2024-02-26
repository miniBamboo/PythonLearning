#使用select找出含有h1标签的元素
from bs4 import BeautifulSoup
html_sample='\
<html> \
    <body> \
    <h1 id="title">hello world</h1> \
    <a href="#" class="link">This is link1</a> \
    <a href="# link2" class="link">This is link2</a> \
    </body> \
</html>'
soup = BeautifulSoup(html_sample,'html.parser')
header = soup.select('h1')
print(header)#回传Python的一个list
print(header[0])#解开这个回传的list，打[0]时没有两边的中括号
print(header[0].text)#只获取里面的文字

print('-'*50)
#使用select找出含有a标签的元素
alink = soup.select('a')
print(alink)
for link in alink:
    print(link)
    print(link.text)
print('-'*50)
#使用select找出所有id为title的元素
alink = soup.select('#title')  #（id前面需加上#）
print(alink)

print('-'*50)
#取得所有a标签内的链接
#使用select找出所有的a tag的href连接
alinks=soup.select('a')
for link in alinks:
    print(link)
    print(link['href'])#用中括号去的里面的词，因为select把取得大部分包装成起来
print('-'*50)

#获取a标签中的不同属性值
a='<a href="#" qoo=123 abc=456> i am a link </a>'
soup2=BeautifulSoup(a, 'html.parser')
#print(link['href'])
print(soup2.select('a'))
print(soup2.select('a')[0])
print(soup2.select('a')[0]['href']) #最后一个中括号里面可以是'abc','qoo','href'，放入不同的属性名称，就可以取得对应的属性值
