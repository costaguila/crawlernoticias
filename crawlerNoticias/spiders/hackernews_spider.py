import scrapy
import datetime

class HackerNewsSpider(scrapy.Spider):
    name = 'HackerNews'
    start_urls = ['https://news.ycombinator.com/',]

    def parse(self,response):
        articles = response.css('.storylink')
        all_news = {
            'name': self.name,
            'dateTime': datetime.datetime.now(),
            'noticias': []
        }
        for item in articles:
            result = {}
            result['image'] = None
            result['title'] = item.css(".storylink::text").extract_first()
            result['crawled_at'] = datetime.datetime.now()
            result['link'] = item.attrib['href']
            result['section'] = 'hacker_news'
            all_news['noticias'].append(result)
        yield all_news
