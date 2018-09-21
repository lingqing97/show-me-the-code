# -*- coding: utf-8 -*-
import scrapy
from picture_spider.items import PictureSpiderItem
from scrapy import Request
class PictureSpiderSpider(scrapy.Spider):
    name = 'picture_spider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    } 
    def start_requests(self):
        start_urls="https://tieba.baidu.com/p/2166231880/"
        yield Request(start_urls,headers=self.headers,callback=self.parse)
    def parse(self, response):
        results=response.xpath("//cc/div/img")
        for result in results:
            try:
                item=PictureSpiderItem()
                item["url"]=result.xpath("./@src").extract_first()
            except:
                continue
            else:
                yield item