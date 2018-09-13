from urllib.request import urlopen
# robots.text文件为网站 的表尊爬虫协议，标注出网站的的那些页面可以抓取。
html = urlopen("https://en.wikipedia.org/robots.text")

print(html.read().decode('utf-8'))