import scrapy
import ipdb
from ..utils.write_result import write_result_to_txt

class g1Spider(scrapy.Spider):
    name = 'g1'
    start_urls = ['https://g1.globo.com']

    def parse(self,response):
        posts = response.css('div.feed-post-body')
        all_news = []
        for item in posts:
            result = {}
            result['image'] = item.css("img.bstn-fd-picture-image::attr('src')").extract_first()
            result['title'] = item.css("a.feed-post-link::text").extract_first()
            result['published_at'] = item.css("span.feed-post-datetime::text").extract_first()
            result['section'] = item.css("span.feed-post-metadata-section::text").extract_first()
            all_news.append(result)
        write_result_to_txt(self.settings.attributes['RESULT_FOLDER'].value,all_news,crawler_name=self.name)
