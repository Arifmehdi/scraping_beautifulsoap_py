import scrapy


class ScrapyscrapSpider(scrapy.Spider):
    name = "scrapyScrap"
    allowed_domains = ["driverbase.com"]
    start_urls = ["https://driverbase.com/"]

    def parse(self, response):
        pass
