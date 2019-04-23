# -*- coding: utf-8 -*-

import pymongo
from douban.settings import mongoHost,mongoPort,mongoName,mongoCollection

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        ## 保存数据到mongoDB数据库，要在setting文件里面开启
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
