import scrapy
from ..utils.write_result import write_result_to_txt

class wsjSpider(scrapy.Spider):
    name = 'wsj'
    start_urls = ['https://www.wsj.com/news/world','https://www.wsj.com/news/economy']

    def parse(self,response):
        articles = response.css('article.hed-summ')
        all_news = []
        for item in articles:
            result = {}
            #Extracting data
            result['title'] = item.css(".hed .headline::text").extract_first()
            result['link'] = item.css("a.headline::attr('href')").extract_first()
            result['summary'] = item.css("p.summary::text").extract_first()
            all_news.append(result)
        write_result_to_txt(self.settings.attributes['RESULT_FOLDER'].value,all_news,crawler_name=self.name)
