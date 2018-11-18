from urllib import request, parse
import urllib
import random


headers_list = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'},
]

user_headers = random.choice(headers_list)

def loadPage(url, file_name):
    """
    爬取数据
    :param url:输入的url, 文件名
    :return:None
    """
    print("正在下载%s" % file_name)
    req = request.Request(url=url, headers=user_headers)

    response = request.urlopen(req)
    return response.read().decode('utf-8')

def writePage(html, file_name):
    """
    html写入文件
    :param html:输入的html
    :return:None
    """
    print("正在保存%s" % file_name)
    with open(file_name, 'w') as f:
        f.write(html)
    print("-" * 30)

def tieBa(url , b_page, s_page):
    """
    贴吧爬虫调度,处理每一个页面
    :return:
    """
    for page in range(int(b_page), (s_page+1)):
        pn = (page-1) *50
        file_name = "第%s页" % page
        full_url = url + '&pn=' + str(pn)
        html = loadPage(full_url, file_name)
        writePage(html, file_name)

if __name__ == "__main__":
    kw = "猫"  #输入的关键字
    b_page = 1 #起始页
    s_page = 1 #结束页
    url = 'https://tieba.baidu.com/f?'

    key = urllib.parse.urlencode({'kw':kw})

    full_url = url + key

    tieBa(full_url, b_page, s_page)
