import requests
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

r1 = requests.get(
    url='https://passport.lagou.com/login/login.html', #?service=https%3a%2f%2fwww.lagou.com%2f
    headers=headers,
)

X_Anit_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]
X_Anit_Forge_Code= re.findall("X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]

r2 = requests.post(
    url='https://passport.lagou.com/login/login.json',
    headers={
        'Host': 'passport.lagou.com',
        'Origin': 'https://passport.lagou.com',
        'Referer': 'https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Anit-Forge-Code': X_Anit_Forge_Code,
        'X-Anit-Forge-Token': X_Anit_Forge_Token,
    },
    data={
        'isValidate': 'true',
        'username': '15435345',
        'password': '65063791cc2f4d5e2ae31a40ab333eaa',
        'request_form_verifyCode':'',
        'submit':'',
        'challenge': 'b12ba7e66d545f1051362bf36e9e498f',
    },
)

print(r2.text)