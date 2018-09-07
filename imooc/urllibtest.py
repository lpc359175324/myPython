from urllib import request

#操作  打开url
#req= request.urlopen("http://www.baidu.com ")

req = request.Request("http://www.baidu.com ")
# 添加agent头判断是否是爬虫
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36www.baidu.com")

resp = request.urlopen(req)

print(resp.read().decode("utf-8"))

