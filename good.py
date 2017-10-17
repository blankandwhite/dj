# -*- coding: utf-8 -*-
import scrapy


class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
