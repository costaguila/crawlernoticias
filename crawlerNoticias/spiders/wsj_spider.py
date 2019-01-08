import scrapy

class wsjSpider(scrapy.Spider):
    name = 'wsj'
    start_urls = ['https://www.wsj.com/news/world','https://www.wsj.com/news/economy']

    def parse(self,response):

        articles = response.css('article.hed-summ')
        for item in articles:
            #Extracting data
            title = item.css(".hed .headline::text").extract_first()
            link = item.css("a.headline::attr('href')").extract_first()
            summary = item.css("p.summary::text").extract_first()
            result = "========\nTitulo: {0}\nsummary: {1}\n link:{2}\n"
            result = result.format(title,summary,link)
            print(result)
