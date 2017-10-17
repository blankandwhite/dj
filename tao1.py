# -*- coding: utf-8 -*-
import scrapy


class Tao1Spider(scrapy.Spider):
    name = 'tao1'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
