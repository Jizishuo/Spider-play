from urllib import request, parse
import urllib

#%E5%89%A7%E6%83%85==剧情片
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90'#&action=&start=40&limit=20
#url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

data = {
    #'type': '11',
    #'interval_id': '100:90',
    'action':'',
    'start': '60',
    'limit': '40',
}
# 数据编码
data = parse.urlencode(data).encode()

req = request.Request(url=url, data=data, headers=headers)

rsp = request.urlopen(req)

html = rsp.read().decode()
print(html)