from scrapy import Request
from scrapy import Spider
from picture_spider.items import PictureSpiderItem

class picture_spider(Spider):
    name="picture_spider"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }   
    def start_requests(self):
        url="http://tieba.baidu.com/p/2166231880"
        yield Request(url,headers=self.headers,callable=self.parse)
    def parse(self,response):
        item=PictureSpiderItem()
        results=response.xpath("//cc/div/img")
        for result in results:
            try:
                item["url"]=' '.join(result.xpath(".src").extract()).strip()
            except:
                continue
            else:
                yield item