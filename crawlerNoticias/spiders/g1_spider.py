import scrapy
import datetime

class G1Spider(scrapy.Spider):
    name = 'G1'
    start_urls = ['https://g1.globo.com']

    def parse(self,response):
        posts = response.css('div.feed-post-body')
        all_news = {
            'name': self.name,
            'dateTime': datetime.datetime.now(),
            'noticias': []
        }
        for item in posts:
            result = {}
            result['image'] = item.css("img.bstn-fd-picture-image::attr('src')").extract_first()
            result['title'] = item.css("a.feed-post-link::text").extract_first()
            result['published_at'] = item.css("span.feed-post-datetime::text").extract_first()
            result['link'] = item.css('.feed-post-link').attrib['href']
            result['section'] = item.css("span.feed-post-metadata-section::text").extract_first()
            all_news['noticias'].append(result)
        yield all_news
