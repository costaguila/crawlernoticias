# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils import project


class MongoDBPipeline(object):
    client = None
    settings = None

    def __init__(self):
        self.settings = project.get_project_settings()
        self.client = pymongo.MongoClient(self.settings['DATABASE']['conn'])

    def  open_spider(self, spider):
        print("#==============================")
        print("# Executanto {}".format(spider.name))
        print("#==============================")

    def process_item(self, item, spider):
        db = self.client[self.settings['DATABASE']['name']]
        db["noticias"].insert_many(item['noticias'])
        print("#==============================")
        print("# Foram encontradas {} noticias em {}".format(len(item['noticias']), spider.name))
        print("#==============================")

        return item

    def close_spider(self, spider):
        print("#==============================")
        print("# Finalizando {}".format(spider.name))
        print("#==============================")
        self.client.close()
