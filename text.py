import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

cookie = {'etone.session.id': '201a977c-08f9-4317-a981-a234d1d40264',
          'rememberMe': '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',
          'JSESSIONID': 'E5D349F0711B881C00EE3373A2AB3816',
          'qs-web': '%7B%22loginId%22%3A%22dwqiumindan%22%2C%22orgName%22%3A%22%E6%97%A0%E4%BC%98%E4%B8%AD%E5%BF%83%22%2C%22uname%22%3A%22dwqiumindan%22%2C%22roleId%22%3A%22yt_34%2CCOMMONE%2CALL_PORTAL_USER_ROLE%22%2C%22mt%22%3A%5B%7B%22cityName%22%3A%22%E5%B9%BF%E5%B7%9E%22%2C%22roleId%22%3A%22yt_34%22%2C%22groupName%22%3A%22%E5%B9%BF%E5%B7%9E%E7%95%AA%E7%A6%BA%E5%8C%BA%2C%E5%B9%BF%E5%B7%9E%E5%BC%80%E5%8F%91%E5%8C%BA%22%7D%5D%2C%22mobile%22%3A%2213560288282%22%2C%22userName%22%3A%22%E9%82%B1%E6%95%8F%E4%B8%B9%22%2C%22yt33Role%22%3A%22%22%2C%22orgId%22%3A%2286020%22%2C%22uid%22%3A%22dwqiumindan%22%2C%22state%22%3A%221%22%2C%22isPass%22%3A%22true%22%2C%22email%22%3A%2213922327501%40139.com%22%7D'
          }

data = {
    'problem_status': '方案确认',
    'city': '广州',
    'area_grid[]': '广州番禺区',
    #'area_grid[]': '广州开发区',
    'question_type': '',
    'data_source': '',
    'special_label': '',
    'role': '市优化网格组员',
    'intdetail_analyse[]': 0,
}

req4 = requests.post(
    url='https://nqi.gmcc.net:20443/ltemr-portal/modules/problemState/queryDatas.do',
    headers=headers,
    cookies=cookie,
    data=data,
)
print(req4.text)