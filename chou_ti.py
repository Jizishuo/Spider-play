import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

#______________________首页————————————————————————————
url = 'https://dig.chouti.com/'
req1 = requests.get(url, headers=headers)
#print(req.text)

soup = BeautifulSoup(req1.text, 'html.parser')

content_list = soup.find(name="div", id='content-list') #attrs={'id':'content-list'}
item_list = content_list.find_all(name='div', attrs={'class':"item"})
#print(item_list)

for item in item_list:
    a = item.find(name='a', attrs={'class':"show-content color-chag"})
    #print(a.text.strip()) #文本加去空格



#______________________登录————————————————————————————
data = {
    'phone': '8615626148050',
    'password': '19950920',
    'oneMonth':'',
}

url = 'https://dig.chouti.com/login'
#登录
req2 = requests.post(
    url,
    headers=headers,
    data=data,
    cookies=req1.cookies.get_dict(), #登录首页的授权cooles
)
#print(req2.text)
print(req2.cookies.get_dict())


#______________________点赞————————————————————————————
# req3 = requests.post(
#     url='https://dig.chouti.com/link/vote?linksId=23232691',
#     headers=headers,
#     cookies=req1.cookies.get_dict(), ##登录首页的授权（登录）好的 cooles
# )
# print(req3.text)

#______________________取消点赞————————————————————————————
req4 = requests.post(
    url='https://dig.chouti.com/vote/cancel/vote.do',
    headers=headers,
    cookies=req1.cookies.get_dict(),
    data={'linksId': '23232691'},
)
print(req4.text)