from scrapy import spiderloader
from scrapy.utils import project
from scrapy.crawler import CrawlerProcess
from utils.user_agents import select_random_usr_agent

#Recupera o nome de todas os crawlers deste projeto
settings = project.get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
spiders = spider_loader.list()
classes = [spider_loader.load(name) for name in spiders]
#Inicia um processo para o crawl
process = CrawlerProcess({
    'USER_AGENT': select_random_usr_agent()
})
#Crawl
for spider_class in classes:
    process.crawl(spider_class)
process.start()
