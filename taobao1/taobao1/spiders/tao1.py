# -*- coding: utf-8 -*-
import scrapy
import

class Tao1Spider(scrapy.Spider):
    name = 'tao1'
    allowed_domains = ['taobao.com']
    start_urls = ['https://taobao.com/']

    def parse(self, response):
        key="nike"
        for i in range(0,10):
            url="https://s.taobao.com/search?q="+str(key)+"&s="+str(i*44)
            yield Request(url=url,callback=self.page)
        pass
    def page(self,response):
        body=response.bady.decode("utf-8","ignore")
        pat='"nid":"(.*?)"'
        allid=re.compile(pat).findall(bady)
        print(allid)