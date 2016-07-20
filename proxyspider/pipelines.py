# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem
from proxyspider.myutils.DBUtil import DBUtil
from proxyspider.items import ProxyServer


class MongoPipeline(object):
    def __init__(self):
        self.dbutil = DBUtil()
        self.proxy_seq = 1

    def open_spider(self, spider):
        self.dbutil.db.drop_collection(ProxyServer.__name__)

    def close_spider(self, spider):
        self.dbutil.closedb()

    def process_item(self, item, spider):
        if isinstance(item, ProxyServer):
            collection_name = ProxyServer.__name__
            item['proxy_seq'] = self.proxy_seq
            self.proxy_seq += 1
            self.dbutil.db[collection_name].insert(dict(item))
            return item
