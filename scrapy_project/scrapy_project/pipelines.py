# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        return item


class PretreatmentPipeline(object):
    def process_item(self, item, spider):
        if item['title']:
            # 不让title为空
            item['title'] = ''
        return item


class DuplicatesPipeline(object):
    def __init__(self):
        self.links = set()

    def process_item(self, item, spider):
        if item['link'] in self.links:
            # 跑出DropItem表示丢掉数据
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.links.add(item['link'])
            return item
