import requests
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent

# 随机一个ua
user = UserAgent()
ua = user.chrome

baseHeaders = {
    'User-Agent': ua,
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def getPage(url, option={}):
    headers = dict(baseHeaders, **option)
    print('正在抓取: ', url)
    try:
        response = requests.get(url, headers=headers)
        print('抓取 {} 成功! '.format(url), response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取 {} 失败', url)
        return None