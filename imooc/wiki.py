#获取维基百科 词条

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

res = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode('utf-8')
soup = BeautifulSoup(res,'html.parser')
# print(soup)
listUrls = soup.findAll('a',href=re.compile("^/wiki/"))
for url in listUrls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text(),"-----","https://en.wikipedia.org"+url["href"])
