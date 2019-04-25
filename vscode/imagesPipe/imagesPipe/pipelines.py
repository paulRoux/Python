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


class ImagesDownloadPipe2(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['image_urls']:
            # 给file_path传递图片名字
            yield scrapy.Request(url, meta={'image_name': item['image_name']})


    def item_completed(self, results, item, info):
        # 将下载的图片路径（传入到results中）存储到 path 项目组中，如果其中没有图片，我们将丢弃项目:
        path = [x['path'] for ok, x in results if ok]
        if not path:
            raise DropItem("Item contains no image")
        item['imagePath'] = path
        return item


    # 修改图片存储的名字
    def file_path(self, request, response=None, info=None):
        file_name = request.meta['image_name']
        file_name = file_name.replace('/', '_')
        return "full/{}.jpg".format(file_name)