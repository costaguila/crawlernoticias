import scrapy
import datetime

class wsjSpider(scrapy.Spider):
    name = 'wsj'
    start_urls = ['https://www.wsj.com/news/world','https://www.wsj.com/news/economy']

    def parse(self,response):
        articles = response.css('article.hed-summ')
        all_news = {
            'name': self.name,
            'dateTime': datetime.datetime.now(),
            'noticias': []
        }
        for item in articles:
            result = {}
            #Extracting data
            result['title'] = item.css(".hed .headline::text").extract_first()
            result['link'] = item.css("a.headline::attr('href')").extract_first()
            result['summary'] = item.css("p.summary::text").extract_first()
            all_news['noticias'].append(result)
        yield all_news
