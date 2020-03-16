from scrapy import Spider
from scrapy.selector import Selector
from DataCrawler.items import DatacrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["https://beatme.pythonanywhere.com/"]
    start_urls = [
        "https://beatme.pythonanywhere.com/",
    ]

    def parse(self, response):
        data = Selector(response).xpath('/html/body/div[2]/div[3]/span/p')
        for x in data:
            item = DatacrawlerItem()
            item['username'] = x.xpath('i/text()').extract_first()
            yield item