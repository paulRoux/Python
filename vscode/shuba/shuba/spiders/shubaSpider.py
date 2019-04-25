# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shuba.items import ShubaItem

class ShubaspiderSpider(CrawlSpider):
    name = 'shubaSpider'
    allowed_domains = ['69shu.com']
    start_urls = ['https://www.69shu.com/795/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='mu_contain'][2]//ul[@class='mulu_list'][1]/li[1]/a")),                   callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='warpper']//table//tr//div//span[4]/a")),
            callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        items = ShubaItem()
        items['title'] = response.xpath("//h1//text()").get()
        items['content'] = ''.join(response.xpath("//div[@class='yd_text2']/text()").extract()).replace('\r\n', '').replace('\xa0\xa0\xa0\xa0', '\n  ')
        # print(items)
        yield items
