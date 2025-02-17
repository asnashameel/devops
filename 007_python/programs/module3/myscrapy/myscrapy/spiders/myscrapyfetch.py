import scrapy

class Extracturls(scrapy.Spider):
    name = "asna"
    def start_requests(self):
        urls = ['https://economictimes.indiatimes.com']
        for u in urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        links=response.css('a::attr(href)').extract()
        for link in links:
            yield({'links':links})