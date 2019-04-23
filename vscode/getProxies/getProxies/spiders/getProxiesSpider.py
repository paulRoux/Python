# -*- coding: utf-8 -*-
import scrapy
from getProxies.items import GetproxiesItem


counter = 0
class GetproxiesspiderSpider(scrapy.Spider):
    name = 'getProxiesSpider'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/wt']

    def parse(self, response):
        proxyList = response.xpath("//table[@id='ip_list']//tr")
        global counter
        if counter > 500:
            ## 这是一个不准确的情况，因为这次没到500，会执行下面的循环导致最终超出500
            print("The data has finished!")
            return
        for item in proxyList[1:]:
            proxyItem = GetproxiesItem()
            proxyItem['proxySpeed'] = item.xpath(".//td[7]/div/@title").extract_first()
            if float(proxyItem['proxySpeed'].replace('秒', "").strip()) > 4.0:
                continue
            counter +=  1
            proxyItem['proxyNum'] = counter
            proxyItem['proxyIp'] = item.xpath(".//td[2]/text()").extract_first()
            proxyItem['proxyPort'] = item.xpath(".//td[3]/text()").extract_first()
            proxyItem['proxyAddr'] = item.xpath(".//td[4]/a[@href]/text()").extract_first()
            proxyItem['proxyType'] = item.xpath(".//td[6]/text()").extract_first()
            proxyItem['proxyConnectTime'] = item.xpath(".//td[8]/div/@title").extract_first()
            proxyItem['proxyAliveTime'] = item.xpath(".//td[9]/text()").extract_first()
            proxyItem['proxyAliveTime'] = item.xpath(".//td[10]/text()").extract_first()

            yield proxyItem

        nextLink = response.xpath("//div[@class='pagination']//a[@class='next_page']/@href").extract_first()
        if nextLink:
            yield scrapy.Request("https://www.xicidaili.com"+nextLink, callback=self.parse)




