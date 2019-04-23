from  lxml import etree
from proxyPool.utils import getPage

class ProxyMetaClass(type):
    """
    代理元类，主要是将各大代理网站的爬取函数进行提取，方便Crawler类的getProxies方法进行调用
    """
    def __new__(cls, name, bases, attr):
        count = 0
        attr['__CrawlFunc__'] = []
        for k, v in attr.items():
            if 'craw' in k:
                attr['__CrawlFunc__'].append(k)
                count += 1
        attr['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attr)

class Crawler(object, metaclass=ProxyMetaClass):
    def getProxies(self, callFunc):
        # 通过getter调用，来进行代理网站的爬取
        proxies = []
        for proxy in eval("self.{}()".format(callFunc)):
            print("成功获取代理 {} ".format(proxy))
            proxies.append(proxy)
        return proxies

    ## 下面是各大免费代理网站的爬取逻辑
    ## 后面可以抽象一个爬取函数出来，供各代理函数使用
    startUrl = ""  ## 开始的url

    def crawXici(self, pageCount = 4):
        startUrl = "https://www.xicidaili.com/wt/"  ## HTTP
        for count in range(pageCount):
            print("开始爬取 {} 第 {} 页".format(startUrl, count+1))
            source = getPage(startUrl)
            html = etree.HTML(source)

            items = html.xpath("//table[@id='ip_list']//tr")
            for item in items[1:]:
                speed = item.xpath(".//td[7]/div/@title")
                if float(speed[0].replace('秒', "").strip()) > 4.0:
                    continue
                ip = item.xpath(".//td[2]/text()")
                port = item.xpath(".//td[3]/text()")
                yield ":".join([ip[0], port[0]])

            nextLink = html.xpath("//div[@class='pagination']//a[@class='next_page']/@href")
            if nextLink:
                startUrl = "https://www.xicidaili.com" + nextLink[0]


    # def crawKuaiDL(self, pageCount = 4):
    #     startUrl = "https://www.kuaidaili.com/free/inha/"  ## HTTP
    #     for count in range(pageCount):
    #         print("开始爬取 {} 第 {} 页".format(startUrl, count+1))
    #         source = getPage(startUrl)
    #         html = etree.HTML(source)

    #         items = html.xpath("//div//div[@id='list']//tbody/tr")
    #         for item in items:
    #             speed = item.xpath(".//td[6]/text()")
    #             if float(speed[0].replace('秒', "").strip()) > 4.0:
    #                 continue
    #             ip = item.xpath(".//td[1]/text()")
    #             port = item.xpath(".//td[2]/text()")
    #             yield ":".join([ip[0], port[0]])

    #         page = count + 1
    #         startUrl = "https://www.kuaidaili.com/free/inha/" + page

    # def crawYunDL(self, pageCount = 4):
    #     if pageCount > 7:
    #         print("最大页数 7 页，已设置为 7 页！")
    #         pageCount = 7
    #     startUrl = "http://www.ip3366.net/free/?stype=1"  ## HTTP && HTTPS
    #     for count in range(pageCount):
    #         print("开始爬取 {} 第 {} 页".format(startUrl, count+1))
    #         source = getPage(startUrl)
    #         html = etree.HTML(source)

    #         items = html.xpath("//div[@id='list']//tbody//tr")
    #         for item in items:
    #             speed = item.xpath(".//td[6]/text()")
    #             if float(speed[0].replace('秒', "").strip()) > 4.0:
    #                 continue
    #             ip = item.xpath(".//td[1]/text()")
    #             port = item.xpath(".//td[2]/text()")
    #             yield ":".join([ip[0], port[0]])

    #         page = count + 1
    #         startUrl = "http://www.ip3366.net/free/?stype=1&page=" + page

    # def crawIp66DL(self, pageCount = 4):
    #     startUrl = "http://www.66ip.cn"  ## HTTP && HTTPS
    #     for count in range(pageCount):
    #         print("开始爬取 {} 第 {} 页".format(startUrl, count+1))
    #         source = getPage(startUrl)
    #         html = etree.HTML(source)

    #         items = html.xpath("//div[@id='main']//tbody//tr")
    #         for item in items:
    #             ip = item.xpath(".//td[1]/text()")
    #             port = item.xpath(".//td[2]/text()")
    #             yield ":".join([ip[0], port[0]])

    #         page = count + 1
    #         startUrl = "http://www.66ip.cn/" + page

    # def crawIp89DL(self, pageCount = 4):
    #     startUrl = "http://www.89ip.cn"  ## HTTP && HTTPS
    #     for count in range(pageCount):
    #         print("开始爬取 {} 第 {} 页".format(startUrl, count+1))
    #         source = getPage(startUrl)
    #         html = etree.HTML(source)

    #         items = html.xpath("//div[@class='layui-form']//tbody//tr")
    #         for item in items:
    #             ip = item.xpath(".//td[1]/text()")
    #             port = item.xpath(".//td[2]/text()")
    #             yield ":".join([ip[0], port[0]])

    #         page = count + 1
    #         startUrl = "http://www.89ip.cn/index_" + page

    # def crawData5u(self, pageCount = 1):
    #     startUrl = 'http://www.data5u.com/free/gngn/index.shtml'
    #     headers = {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #         'Accept-Encoding': 'gzip, deflate',
    #         'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    #         'Cache-Control': 'max-age=0',
    #         'Connection': 'keep-alive',
    #         'Cookie': 'JSESSIONID=694DB8BC18C0697975ABD4D10A216C38',
    #         'Host': 'www.data5u.com',
    #         'Referer': 'http://www.data5u.com/free/index.shtml',
    #         'Upgrade-Insecure-Requests': '1',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    #     }

    #     for count in range(pageCount):
    #         print("开始爬取 {} 第 {} 页".format(startUrl, count+1))
    #         source = getPage(startUrl, option=headers)
    #         html = etree.HTML(source)

    #         items = html.xpath("//div[@class='wlist']//li//ul")
    #         for item in items[1:]:
    #             speed = item.xpath(".//span[8]/li/text()")
    #             if float(speed[0].replace('秒', "").strip()) > 4.0:
    #                 continue
    #             ip = item.xpath(".//span[1]/li/text()")
    #             port = item.xpath(".//span[2]/li/text()")
    #             yield ":".join([ip[0], port[0]])
