import json
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from cookiesProxy.dataBase import RedisClient
from login.weibo.cookies import WeiboCookies
from cookiesProxy.config import BROWSER_TYPE


class CookiesGenerator():
    def __init__(self, websites="website"):
        """
        父类, 初始化一些对象
        :param websites: 名称
        :param browser: 浏览器, 若不使用浏览器则可设置为 None
        """
        self.websites = websites
        self.cookiesDb = RedisClient("cookies", self.websites)
        self.accountDb = RedisClient("accounts", self.websites)
        self.initBrowser()


    def __del__(self):
        self.close()


    def initBrowser(self):
        """
        通过browser参数初始化全局浏览器供模拟登录使用
        :return:
        """
        if BROWSER_TYPE == "PhantomJS":
            caps = DesiredCapabilities.PHANTOMJS
            caps[
                "phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
            self.browser = webdriver.PhantomJS(desired_capabilities=caps)
            self.browser.set_window_size(1400, 500)
        elif BROWSER_TYPE == 'Chrome':
            self.browser = webdriver.Chrome()


    def newCookies(self, username, password):
        """
        新生成Cookies，子类需要重写
        :param username: 用户名
        :param password: 密码
        :return:
        """
        raise NotImplementedError


    def processCookies(self, cookies):
        """
        处理Cookies
        :param cookies:
        :return:
        """
        dicts = {}
        for cookie in cookies:
            dicts[cookie["name"]] = cookie["value"]
        return dicts


    def run(self):
        """
        运行, 得到所有账户, 然后顺次模拟登录
        :return:
        """
        accountUsername = self.accountDb.username()
        cookiesUsername = self.cookiesDb.username()

        for username in accountUsername:
            if not username in cookiesUsername:
                password = self.accountDb.get(username)
                print("正在生成Cookies！ 账号 {} 密码 {}".format(username, password))
                result = self.newCookies(username, password)
                # 成功获取
                if result.get("status") == 1:
                    cookies = self.processCookies(result.get("content"))
                    print("成功获取到Cookies：", cookies)
                    if self.cookiesDb.set(username, json.dumps(cookies)):
                        print("成功保存Cookies！")
                # 密码错误，移除账号
                elif result.get("status") == 2:
                    print(result.get("content"))
                    if self.accountDb.delete(username):
                        print("成功删除账号！")
                else:
                    print(result.get("content"))
        else:
            print("所有账号都已经获取了Cookies！")


    def close(self):
        """
        关闭
        :return:
        """
        try:
            print("Closing browser!")
            self.browser.close()
            del self.browser
        except TypeError:
            print("Browser is not opened!")


class WeiboCookiesGenerator(CookiesGenerator):
    def __init__(self, websites="weibo"):
        """
        初始化操作
        :param websites: 站点名称
        :param browser: 使用的浏览器
        """
        CookiesGenerator.__init__(self, websites)
        self.websites = websites

    def newCookies(self, username, password):
        """
        生成Cookies
        :param username: 用户名
        :param password: 密码
        :return: 用户名和Cookies
        """
        return WeiboCookies(username, password, self.browser).main()


if __name__ == "__main__":
    generator = WeiboCookiesGenerator()
    generator.run()
