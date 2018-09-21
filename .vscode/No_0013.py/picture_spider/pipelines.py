# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urllib.request import urlopen

class PictureSpiderPipeline(object):
    i=0
    def process_item(self, item, spider):
        try:
            data=urlopen(str(item["url"])).read()
            path=".\\picture\\"+str(self.i)+".jpg"   #图片存放路径
            file=open(path,"wb")
            file.write(data)
            file.close()
            self.i=self.i+1
        except:
            return item
        else: 
            return item