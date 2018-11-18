
from urllib import request, parse
import urllib
import random

headers_list = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'},

]

dict = {
    'name': 'zhaofan'
}

user_headers = random.choice(headers_list)

'''
#url = 'https://www.baidu.com'
url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=02003390_9_hao_pg&wd=%E7%8C%AB%E8%96%84%E8%8D%B7&oq=%25E7%258C%25AB%25E8%2596%2584%25E8%258D%25B7&rsv_pq=cf1f209d0005ec73&rsv_t=f968vVCThCE8wylKxL0NtzY%2F8X8kbJ0VM0%2FvT1qbnzrYEKEcDclYmSVcgFJOMOfZg5TCBXmhrzA&rqlang=cn&rsv_enter=0&prefixsug=%25E7%258C%25AB%25E8%2596%2584%25E8%258D%25B7&rsp=0&rsv_sug9=es_0_1&rsv_sug=9&rsv_jmp=slow'

print(user_headers)
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, headers=user_headers)

#response = request.urlopen(req)
#print(response.read().decode('utf-8'))

# print(response.geturl())
# print("---------------------------------------")
# print(response.info())
# print("---------------------------------------")
# print(response.getcode())
# print("---------------------------------------")
#print(response.header())
'''

# a = urllib.parse.urlencode({'sss':'测试'})
# print(a) #sss=%E6%B5%8B%E8%AF%95
# b = urllib.parse.unquote(a)
# print(b) #sss=测试

url = 'https://www.baidu.com/s'

keywords = "猫"
wd = {'wd': keywords}

wd = urllib.parse.urlencode(wd)

full_url = url + '?' + wd
print(full_url)

req = request.Request(url=url, headers=user_headers)

response = request.urlopen(req)
print(response.read().decode('utf-8'))

