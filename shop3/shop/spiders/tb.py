# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import ssl
from scrapy.http import Request
import re
from shop.items import ShopItem
import pymysql
class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["airbnb.com"]
    start_urls = (
        'https://zh.airbnb.com/',
    )

    def parse(self, response):
        key="Sydney--New-South-Wales--Australia"
        for i in range(0,5):
            url="https://zh.airbnb.com/s/"+str(key)+"&section_offset=i"
            yield Request(url=url,callback=self.page)
    def page(self,response):
        #title=response.xpath("/html/head/title").extract()
        body=response.body.decode("utf-8","ignore")
        patid='class="anchor_surdeb"href="/rooms/(.*?)\?'
        allid=re.compile(patid).findall(body)
        print(len(allid))
        #print(allid)
        # for j in range(0,len(allid)):
        #     thisid=allid[j]
        #     url1="https://item.taobao.com/item.htm?id="+str(thisid)
        #     yield Request(url=url1,callback=self.next)
    def next(self,response):
        item=ShopItem()
        yield item