# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class ImagespipePipeline(object):
    def process_item(self, item, spider):
        return item


class ImagesDownloadPipe(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['imageUrl']:
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        # 将下载的图片路径（传入到results中）存储到 path 项目组中，如果其中没有图片，我们将丢弃项目:
        path = [x['path'] for ok, x in results if ok]
        if not path:
            raise DropItem("Item contains no image")
        item['imagePath'] = path
        return item