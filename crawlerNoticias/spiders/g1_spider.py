import scrapy
import ipdb

class g1Spider(scrapy.Spider):
    name = 'g1'
    start_urls = ['https://g1.globo.com']

    def parse(self,response):
        print(response.url)
        posts = response.css('div.feed-post-body')
        for item in posts:
            img_url = item.css("img.bstn-fd-picture-image::attr('src')").extract_first()
            title = item.css("a.feed-post-link::text").extract_first()
            posted_at = item.css("span.feed-post-datetime::text").extract_first()
            section = item.css("span.feed-post-metadata-section::text").extract_first()
            chapeu = item.css('.feed-post-header-chapeu::text').extract_first()
            result = "========\nimg: {0}\nTitulo: {1}\nPostado em: {2}\t seção:{3}\nChapeu: {4}\t\n"
            result = result.format(img_url,title,posted_at,section,chapeu)
            print(result)
