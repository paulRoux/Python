# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanspiderSpider(scrapy.Spider):
    ## 爬虫名
    name = 'doubanSpider'
    ## 允许的域名
    allowed_domains = ['movie.douban.com']
    ## 入口的url，会传入调度器
    start_urls = ['https://movie.douban.com/top250']

    ## 默认解析方法
    def parse(self, response):
        ## 循环电影的条目
        moiveList = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for item in moiveList:
            ## item文件导进来
            doubanItem = DoubanItem()
            ## 写详细的xpath进行数据解析
            doubanItem['serialNumber'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            print(doubanItem)
            doubanItem['movieName'] = item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()

            ## 遇到多行的数据进行处理
            contents = item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()
            for content in contents:
                cont = "".join(content.split())
                doubanItem['introduce'] = cont

            doubanItem['star'] = item.xpath(".//span[@class='rating_num']/text()").extract_first()
            doubanItem['evaluate'] = item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            doubanItem['describe'] = item.xpath(".//p[@class='quote']/span/text()").extract_first()

            ## 需要将数据yield到pipelines里面
            yield doubanItem

        ## 解析下一页，取后一页的xpath
        nextLink = response.xpath("//span[@class='next']/link/@href").extract()
        if nextLink:
            nextLink = nextLink[0]
            ## 将下一个url返回进行解析
            yield scrapy.Request("https://movie.douban.com/top250"+nextLink, callback=self.parse)