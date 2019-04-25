import requests
from fake_useragent import UserAgent
from lxml import etree


"""
大体的爬虫框架，每个类对应一个模块，全局的数据抽出一个配置文件
 """


headers = {
    "User-Agent": UserAgent().chrome
}


class UrlManager(object):
    def __init__(self):
        self.newUrl = []
        self.oldUrl = []


    def getUrl(self):
        url = self.newUrl.pop()
        self.oldUrl.append(url)
        return url


    def addUrl(self, url):
        if url not in self.newUrl and url and url in self.oldUrl:
            self.newUrl.append(url)


    def addUrls(self, urls):
        for url in urls:
            if url not in self.newUrl and url and url in self.oldUrl:
                self.newUrl.append(url)


    def getUrlsize(self):
        return len(self.newUrl)


    def hasUrl(self):
        return self.getUrlsize > 0


    def getOldUrlSize(self):
        return len(self.oldUrl)


class Downloader(object):
    def download(self, url):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding("utf-8")
            return response.text
        else:
            return None


class Parser(object):
    def parse(self, html):
        e = etree.HTML(html)
        datas = self.parseData(e)
        urls = e.xpath()
        return datas, urls

    def parseData(self, e):
        datas = []
        # data = e.xpath()
        # for d int data:
        #     pass
        return datas


    def parseUrl(self, e):
        urls = []
        # url = e.xpath()
        # for u int url:
        #     pass
        return urls


class DataHandler(object):
    def save(self, datas):
        # for data in datas:
        #     """ DB操作 或者 文件操作 """
        #     pass
        pass


class Scheduler(object):
    def __init__(self):
        self.downloader = Downloader()
        self.urlManager = UrlManager()
        self.parser = Parser()
        self.dataHandler = DataHandler()


    def run(self, url):
        self.urlManager.addUrl(url)
        while self.urlManager.hasUrl():
            url = self.urlManager.getUrl()
            html = self.downloader.download(url)
            data, urls = self.parser.parse(html)
            self.dataHandler.save(data)
            self.urlManager.addUrls(urls)


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run("https://www.baidu.com")