# -*- coding: utf-8 -*-
import scrapy
from items import TestUseproxyItem

class GetmyipSpider(scrapy.Spider):
    name = 'getmyip'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']


    def parse(self, response):
       try:
            raw_datastr = str(response.text).replace(' ', '').replace('\n','').replace('{','').replace('}','').replace('"','').split(':')
            raw_datadict = dict([raw_datastr])
            title = raw_datastr[0]
            myip = raw_datadict.get("origin", 'err: not found')
            item = TestUseproxyItem()
            item['title'] = title
            item['myip'] = myip
            yield item
            
       except Exception as e:
            print(e)
      
        
        
