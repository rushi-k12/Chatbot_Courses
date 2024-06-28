import scrapy
from ..items import BrainloxItem

class BrainloxSpiderSpider(scrapy.Spider):
    name = 'brainlox_spider'
    start_urls = [
        'https://brainlox.com/courses/category/technical'
    ]

    def parse(self, response):
        items = BrainloxItem()

        name = response.css('.courses-content a::text').extract()
        price = response.css('.price-per-session::text').extract()
        lessons = response.css('.align - items - center li: nth - child(1)::text').extract()

        for name, price in zip(name, price):
            items['name'] = name
            items['price'] = price
            yield items
