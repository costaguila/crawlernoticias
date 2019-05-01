# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MongoDBPipeline(object):

    def  open_spider(self, spider):
        print("#==============================")
        print("# Executanto {}".format(spider.name))
        print("#==============================")

    def process_item(self, item, spider):
        print("#==============================")
        print("# Foram encontradas {} noticias".format(len(item['noticias'])))
        print("#==============================")
        return item

    def close_spider(self, spider):
        print("#==============================")
        print("# Finalizando {}".format(spider.name))
        print("#==============================")
