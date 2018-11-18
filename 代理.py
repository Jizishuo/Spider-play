import requests

#无验证代理

prexir_dict = {
    'http':'代理一',
    'https':'代理2',
    'https/wwww.7777':'代理3',
}
ret = requests.get(url='',proxies=prexir_dict)

#验证代理
prexir_dict2 = {
    'http':'代理一',
    'https':'代理2',
    'https/wwww.7777':'代理3',
}

from requests.auth import HTTPProxyAuth
auth = HTTPProxyAuth('用户名','密码')

ret2 = requests.get(
    url='',
    proxies=prexir_dict,
    auth=auth
)

#文件上传 (定制文件名)
file_dict = {
    'f1':('text.txt', open('xxx', 'rb')),
}
requests.post(url='', files=file_dict)


#无页面验证（类似路由器）(浏览器做的) 加密用户名密码放请求头 给后台
#请求头 'Authorization : 'basic base64(用户名:密码)'
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

ret3 = requests.get(url='', auth=HTTPBasicAuth('用户名', '密码'))

#超时 timeout

#重定向 allow_redirects
requests.get(url='', allow_redirects=False)

#大文件下载 stream(一点一点取)
from contextlib import closing
with closing(requests.get(url='', stream=True)) as r:
    for i in r.iter_content():
        print(i)
        i.write()

#携带自定义正书 cert
requests.get(url='', cert='xx/xxx/xx.pem')
#证书加密 前边证书，后边秘钥
requests.get(url='', cert=('xx/xxx/xx.pem', 'xxx/xxx/xxx.key'))

#证书确认  verify=False


#request 的 session (自动保存cooikes)