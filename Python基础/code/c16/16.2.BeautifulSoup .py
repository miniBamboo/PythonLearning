#简单的BeautifulSoup示例
from bs4 import BeautifulSoup
html_sample='\
<html> \
    <body> \
    <h1 id="title">hello world</h1> \
    <a href="#" class="link">This is link1</a> \
    <a href="# link2" class="link">This is link2</a> \
    </body> \
</html>'

soup=BeautifulSoup(html_sample,'html.parser')#指定解析器html.parser
print(soup) #没有去掉标签
print(soup.text) #把里面的内容截取出来，而去掉标签

