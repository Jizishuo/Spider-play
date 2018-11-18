import urllib.request
import urllib.parse

url = 'https://weibo.com/u/2651772073/home?wvr=5&c=spr_web_360_hao360_weibo_t002'

#url = 'https://multimedia.api.weibo.com/2/multimedia/user/play_history/report.json?source=2637646381&play_type=0&video_orientation=vertical&video_duration=6&id=4307256860152410&id_type=0&seconds=1&oid=1034:4307256851009332'

# 携带cookie进行访问
headers = {
    # 'Accept':'*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Connection':'keep-alive',
    # 'Content-Length':'13',
    # 'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'INAGLOBAL=4663735975734.4375.1532160173016; __guid=15428400.2132887419694673000.1532246611471.5298; UOR=,,spr_web_360_hao360_weibo_t001; Ugrow-G0=169004153682ef91866609488943c77f; login_sid_t=dc3a79d1212674b70290fc6694a3466f; cross_origin_proto=SSL; YF-V5-G0=d45b2deaf680307fa1ec077ca90627d1; WBStorage=f44cc46b96043278|undefined; wb_view_log=1366*7681; _s_tentry=passport.weibo.com; Apache=28222553727.96789.1542415567320; ULV=1542415567328:23:1:1:28222553727.96789.1542415567320:1540193286465; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5aobPOfpdD.snKz_a7Iyu45JpX5K2hUgL.FozcSK2NS0z7S0e2dJLoIpXLxKMLB.2LB-2LxKqLBKzL1KeLxKML1heL1h8B-5tt; ALF=1573951476; SSOLoginState=1542415477; SCF=AnNI-_O6PCLgnT8XLosCkiRTkQqcCXC74qLoIAtlK_Em0TT4D2_kNDsJGbCFB3MdGZqHgXFw4Pc08qRvFf5TvTg.; SUB=_2A2526xQlDeRhGeRI7lMW9yzMzD-IHXVVgQLtrDV8PUNbmtANLXfYkW9NUrw6H4u73zWt6gCAw-qwweOsgON6h246; SUHB=05i7bHhj07nLRE; un=15626148050; wvr=6; wb_view_log_2651772073=1366*7681; YF-Page-G0=7b9ec0e98d1ec5668c6906382e96b5db; monitor_count=5',
    #'Host':'weibo.com',
    #'Origin':'https://weibo.com',
    #'Referer:https':'//weibo.com/u/2651772073/home?wvr=5&c=spr_web_360_hao360_weibo_t001',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
    #'X-Requested-With':'XMLHttpRequest',

}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# 输出所有
print(response.read().decode('utf-8'))
#print(response.read())

