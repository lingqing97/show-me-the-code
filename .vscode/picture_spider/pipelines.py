# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urllib.request import urlopen
class PictureSpiderPipeline(object):
    i=0
    counter=0
    def process_item(self, item, spider):
        try:
            temp_url='http:'+item['url']
            data=urlopen(temp_url).read()
            if data:
                self.i+=1
                path=str(self.i)+'.jpg'
                self.f=open('D:\\360Downloads\\GitHub客户端code\\show-me-the-code\.vscode\\No_0013_picture\\'+path,'wb')
                self.f.write(data)
        except:
            pass
        return item
