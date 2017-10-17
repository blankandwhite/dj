# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShopPipeline(object):
    def __init__(self):
    def process_item(self, item, spider):
        try:
            title=item["title"][0]
            link=item["link"]
            price=item["price"][0]
            comment=item["comment"][0]
            self.conn.query(sql)
            return item
        except Exception as e:
            pass




