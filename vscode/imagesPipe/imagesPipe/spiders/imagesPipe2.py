# -*- coding: utf-8 -*-
import scrapy
from imagesPipe.items import ImagespipeItem


class Imagespipe2Spider(scrapy.Spider):
    name = 'imagesPipe2'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/7369_91271_2.html']

    def parse(self, response):
        item = ImagespipeItem()
        item['image_urls'] = response.xpath("//div[@class='photo']//img[@id='bigImg']/@src").extract()
        item['image_name'] = response.xpath("//div//h3/a/text()").extract_first() + \
            response.xpath("string(//div//h3/span)").extract_first()
        yield item

        nextUrl = response.xpath("//div[@class='photo']//div//a[@id='pageNext']/@href").extract_first()
        if nextUrl.find('.html') != -1:
            yield scrapy.Request(response.urljoin(nextUrl), callback=self.parse)
