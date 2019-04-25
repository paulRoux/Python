# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShubaPipeline(object):
    def open_spider(self, spider):
        self.file = open("雪中悍刀行.txt", 'w', encoding='utf-8')


    def process_item(self, item, spider):
        title = item['title']
        content = item['content'] + '\n' + '\n'
        info = title + '\n'
        self.file.write(info)
        self.file.write(content)
        self.file.flush()
        return item


    def close_spider(self, spider):
        self.file.close()
