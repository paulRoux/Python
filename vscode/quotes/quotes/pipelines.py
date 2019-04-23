# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from quotes.settings import MONGO_HOST, MONGO_DB


class QuotesPipeline(object):
    def process_item(self, item, spider):
        return item

class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + "..."
            return item
        else:
            return DropItem("Missing Text")


class MongoPipeline(object):
    def __init__(self, mongoUri, mongoDb):
        self.monogoUri = mongoUri
        self.mongoDb = mongoDb

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongoUri = crawler.settings.get("MONGO_HOST"),
            mongoDb = crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.monogoUri)
        self.db = self.client[self.mongoDb]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()