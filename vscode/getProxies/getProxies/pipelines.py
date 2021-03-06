# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from getProxies.settings import mongoHost,mongoPort,mongoName,mongoCollection

class GetproxiesPipeline(object):
    def __init__(self):
        host = mongoHost
        port = mongoPort
        dbname = mongoName
        sheetname = mongoCollection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]


    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
