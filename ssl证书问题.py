import ssl
import urllib
from urllib import request, parse

context = ssl._create_unverified_context()

url = 'https://www.12306.cn/index/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

req = request.Request(url=url, headers=headers)

rsp = request.urlopen(req)

html = rsp.read().decode()

print(html)