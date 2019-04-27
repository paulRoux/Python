# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseItem(scrapy.Item):
    # 类型
    type = scrapy.Field()
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 几居室(列表)
    rooms = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 是否在售
    sale = scrapy.Field()
    # 详情页面
    originUrl = scrapy.Field()


class EsfHouseItem(scrapy.Item):
    # 类型
    type = scrapy.Field()
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 几居室
    rooms = scrapy.Field()
    # 层
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 总价格
    price = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 详情页面
    originUrl = scrapy.Field()


class ZuHouseItem(scrapy.Item):
    # 类型
    type = scrapy.Field()
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 出租类型
    rentType = scrapy.Field()
    # 几居室
    rooms = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 区域
    district = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 交通
    traffic = scrapy.Field()
    # 单价
    price = scrapy.Field()
    # 详情页面
    originUrl = scrapy.Field()
