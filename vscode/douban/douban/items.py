# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ## 序号
    serialNumber = scrapy.Field()
    ## 名称
    movieName = scrapy.Field()
    ## 介绍
    introduce = scrapy.Field()
    ## 星级
    star = scrapy.Field()
    ## 评论数
    evaluate = scrapy.Field()
    ## 描述
    describe = scrapy.Field()

