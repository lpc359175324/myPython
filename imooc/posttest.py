from urllib.request import urlopen
from urllib.request import Request
from urllib import  parse

req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postDate = parse.urlencode([
    ("StartStation","977abb69-413a-4ccf-a109-0272c24fd490"),
    ("EndStation","9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
    ("SearchDate","2018/08/31"),
    ("SearchTime","14:00"),
    ("SearchWay","DepartureInMandarin")
])

req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
req.add_header("Origin","http://www.thsrc.com.tw")

resp = urlopen(req,data=postDate.encode("utf-8"));

print(resp.read().decode("utf-8"))