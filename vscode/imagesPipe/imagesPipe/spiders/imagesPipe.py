# -*- coding: utf-8 -*-
import scrapy

from imagesPipe.items import ImagespipeItem

class ImagespipePySpider(scrapy.Spider):
    name = 'imagesPipe'
    allowed_domains = ['www.freebuf.com']
    start_urls = ['http://www.freebuf.com/']

    def parse(self, response):
        self.log(response.headers)

        picList = response.xpath("//div[@class='news-img']/a/img/@src").extract()
        if picList:
            item = ImagespipeItem()
            item['imageUrl'] = picList
            yield item
