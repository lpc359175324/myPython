#获取维基百科 词条存入 mysql
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import  pymysql.cursors

res = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode('utf-8')
soup = BeautifulSoup(res,'html.parser')
# print(soup)

listUrls = soup.findAll('a',href=re.compile("^/wiki/"))
for url in listUrls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text(),"-----","https://en.wikipedia.org"+url["href"])
        # 链接数据库,获取连接
        connection = pymysql.connect(host='118.89.242.225',user='root',password='789456',db='wikiurl',charset='utf8mb4')
        try:
            #获取会话指针
            with connection.cursor() as cursor:
                sql = "insert into `urls` (`urlname` , `urlhref`) values (%s ,%s )"
                #执行sql语句
                cursor.execute(sql,(url.get_text(),"https://en.wikipedia.org"+url["href"]))
                # 提交
                connection.commit()
        finally:
            # 关闭链接
            connection.close()
















