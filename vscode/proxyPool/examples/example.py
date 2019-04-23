import os
import sys
import requests

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir)


PROXY_POOL_URL = 'http://localhost:5555/random'
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


def crawl(url, proxy):
    proxies = {'http': proxy}
    r = requests.get(url, proxies=proxies)
    return r.text


def main():
    proxy = get_proxy()
    html = crawl('http://docs.jinkan.org/docs/flask/', proxy)
    print(html)

if __name__ == '__main__':
    main()
