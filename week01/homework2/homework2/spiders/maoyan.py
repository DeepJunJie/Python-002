import scrapy
from scrapy.selector import Selector
from homework2.items import Homework2Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # start_urls = ['http://maoyan.com/']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        start_url = "https://maoyan.com/films?showType=3"
        yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response):
        text = response.text.replace("<dd>", "</dd><dd>")
        # print(response.text)
        movies = Selector(text=text).xpath('//div[@class="movies-list"]/dl/dd')

        count = 10
        for movie in movies:
            item = Homework2Item()
            print("################################")
            movie_item = movie.xpath("./div[@class='channel-detail movie-item-title']")
            movie_title = movie_item.xpath('./@title')
            movie_link = movie_item.xpath('./a/@href')
            print(movie_title.extract())
            # print(movie_link.extract())
            item['title'] = movie_title.extract()
            link = 'https://maoyan.com' + movie_link.extract_first()
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
            count -= 1
            if count == 0:
                break

    def parse2(self, response):
        item = response.meta['item']
        movie_type = Selector(response).xpath("//div[@class='movie-brief-container']//a/text()")
        print(movie_type.extract())
        plan_date = Selector(response).xpath("//div[@class='movie-brief-container']//ul/li[3]/text()")
        print(plan_date.extract())
        item['type'] = movie_type.extract()
        item['date'] = plan_date.extract()
        yield item

