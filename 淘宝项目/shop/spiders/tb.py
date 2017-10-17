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
    allowed_domains = ["taobao.com"]
    start_urls = (
        'https://www.taobao.com/',
    )

    def parse(self, response):
        key=["李宁","nike"]
        for k in range(0,2):
            for i in range(0,2):
                url="https://s.taobao.com/search?q="+str(key[k])+"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170823&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s="+str(44*i)
                #ip(ippools)
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
        # title=item["title"][0]
        item["link"]=response.url
        print(item["link"])
        item["price_2"]=response.xpath("//h3[@class='spec-title']/@text()").extract()
        print(item["price_2"])
        item["price"]=response.xpath("//input[@name='current_price']/@value").extract()
        print(item["price"])
        # price=item["price"][0]
        patid='id=(.*?)$'
        thisid=re.compile(patid).findall(response.url)[0]
        commenturl="https://rate.taobao.com/detailCount.do?callback=jsonp100&itemId="+str(thisid)
        # print ("")
        ssl._create_default_https_context=ssl._create_unverified_context
        commentdata=urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
        pat='"count":(.*?)}'
        item["comment"]=re.compile(pat).findall(commentdata)
        # comment=item["comment"][0]

        yield item