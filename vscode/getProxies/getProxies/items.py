# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetproxiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    proxyNum = scrapy.Field()
    proxyIp = scrapy.Field()
    proxyPort = scrapy.Field()
    proxyAddr = scrapy.Field()
    proxyType = scrapy.Field()
    proxySpeed = scrapy.Field()
    proxyConnectTime = scrapy.Field()
    proxyAliveTime = scrapy.Field()
    proxyCheckTime = scrapy.Field()