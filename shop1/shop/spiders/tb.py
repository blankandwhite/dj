# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import ssl
from scrapy.http import Request
import re
from shop.items import ShopItem
import pymysql
from twisted.internet import reactor

reactor.suggestThreadPoolSize(30)
class TbSpider(scrapy.Spider):
    name = "tb"
    allowed_domains = ["taobao.com"]
    #start_urls = ('https://www.taobao.com/')

    def parse(self, response):
        key="nike"
        for i in range(0,1):
            url=""
            yield Request(url=url,callback=self.page)
    def page(self,response):
        #title=response.xpath("/html/head/title").extract()
        body=response.body.decode("utf-8","ignore")
        patid='"nid":"(.*?)"'
        allid=re.compile(patid).findall(body)
        #print(allid)
        for j in range(0,len(allid)):
            thisid=allid[j]
            url1="https://item.taobao.com/item.htm?id="+str(thisid)
            yield Request(url=url1,callback=self.next)
    def next(self,response):
        item=ShopItem()
        item["title"]=response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
        patid='id=(.*?)$'
        thisid=re.compile(patid).findall(response.url)[0]
        commenturl="https://rate.taobao.com/detailCount.do?callback=jsonp100&itemId="+str(thisid)
        #print ("####")
        ssl._create_default_https_context=ssl._create_unverified_context
        commentdata=urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
        pat='"count":(.*?)}'
        item["comment"]=re.compile(pat).findall(commentdata)

        yield item