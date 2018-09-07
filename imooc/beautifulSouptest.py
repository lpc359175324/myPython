from bs4 import BeautifulSoup
import re
# BeautifulSoup API
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#FAQ   .string 标签内包含其他标签返回none      .get_text()返回所有text文本
soup = BeautifulSoup(html_doc,"html.parser");
# 打印soup对象
# print(soup.prettify())

#获取title
print(soup.title)
print(soup.title.string)
print(soup.find(id='link2').string)
# print(soup.find_all('a').get_text())

# 获取所有<a>内容，链接
for link in soup.findAll('a'):
    print(link.string)
    print(link.get('href'))

print(soup.find('p',{ 'class' : 'story'}).get_text())

for tag in soup.find_all(re.compile("^b")):
    print(tag.name)














