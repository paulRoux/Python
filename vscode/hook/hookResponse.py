import requests

def getKeyInfo(response, *args, **kwargs):
    "回调函数"
    print(response.headers['Content-Type'])


def main():
    "主程序"
    requests.get('https://www.baidu.com', hooks = dict(response = getKeyInfo))

if __name__ == '__main__':
    main()