# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter


class SoufangPipeline(object):
    def __init__(self):
        self.newHouseFd = open("E:/code/Python/vscode/soufang/newhouse.json", 'wb')
        self.esfHouseFd = open("E:/code/Python/vscode/soufang/esfhouse.json", 'wb')
        self.zuHouseFd = open("E:/code/Python/vscode/soufang/zuhouse.json", 'wb')
        self.newHouseExporter = JsonItemExporter(self.newHouseFd, ensure_ascii=False)
        self.esfHouseExporter = JsonItemExporter(self.esfHouseFd, ensure_ascii=False)
        self.zuHouseExporter = JsonItemExporter(self.zuHouseFd, ensure_ascii=False)


    def process_item(self, item, spider):
        type = item['type']
        if type == "new":
            self.newHouseExporter.export_item(item)
        elif type == "esf":
            self.esfHouseExporter.export_item(item)
        else:
            self.zuHouseExporter.export_item(item)
        return item


    def close_spider(self, spider):
        self.newHouseFd.close()
        self.esfHouseFd.close()
        self.zuHouseFd.close()
