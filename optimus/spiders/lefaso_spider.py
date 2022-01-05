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
        for article in response.css('div[class="col-xs-12 col-sm-12 col-md-6 col-lg-6"]'):
            yield {
                'title' : article.css('a[href^="spip.php?article1"]::text').get(),
            }