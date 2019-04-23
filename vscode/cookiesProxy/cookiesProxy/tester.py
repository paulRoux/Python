import json
import requests
from requests.exceptions import ConnectionError
from cookiesProxy.dataBase import RedisClient
from cookiesProxy.config import TEST_URL_MAP


class ValidTester(object):
    """
    作为测试的基类，后面每个网站继承
    """
    def __init__(self, websites="website"):
        self.websites = websites
        self.cookiesDb = RedisClient("cookies", self.websites)
        self.accountsDb = RedisClient("accounts", self.websites)


    def test(self, username, password):
        raise NotImplementedError


    def run(self):
        cookiesGroup = self.cookiesDb.all()
        for username, cookies in cookiesGroup.items():
            self.test(username, cookies)


class WeiboValidTester(ValidTester):
    def __init__(self, websites='weibo'):
        ValidTester.__init__(self, websites)

    def test(self, username, cookies):
        print('正在测试 {} 的Cookies!'.format(username))
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('{} 的Cookies不合法!'.format(username))
            self.cookiesDb.delete(username)
            print('删除 {} 的Cookies!'.format(username))
            return
        try:
            test_url = TEST_URL_MAP[self.websites]
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('{} Cookies有效!'.format(username))
            else:
                print(response.status_code, response.headers)
                print('{} 的Cookies失效!'.format(username))
                self.cookiesDb.delete(username)
                print('删除 {} 的Cookies!'.format(username))
        except ConnectionError as e:
            print('发生异常!', e.args)


if __name__ == "__main__":
    WeiboValidTester().run()