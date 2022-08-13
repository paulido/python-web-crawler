import scrapy


class LefasoSpider(scrapy.Spider):
    name = "lefaso"

    def start_requests(self):
        urls = [
            'https://lefaso.net/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css("h3 a::text"):
            yield {
                'title' : article.getall(),
            }