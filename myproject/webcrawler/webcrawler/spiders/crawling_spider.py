#https://youtu.be/m_3gjHGxIJc?si=VdBeKBK5FtfxNRjy
#https://docs.scrapy.org/en/latest/intro/tutorial.html
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from webcrawler.items import DownfilesItem

class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Information_retrieval"]

    custom_settings = {
        "DEPTH_LIMIT": 10,
        "CLOSESPIDER_PAGECOUNT" : 2500
    } 

    rules = (
        Rule(LinkExtractor(allow="wiki/"), callback="parse_link", follow=True),
        #Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_book"),
        #Rule(LinkExtractor(allow=["page"], deny="tag"), callback="parse_quote")
    )

    def parse_link(self, response):
        file_url = response.css('.mw_content_container a::attr(href)').get()
        file_url = response.urljoin(file_url)
        item = DownfilesItem()
        item['file_urls'] = [file_url]
        yield item
'''
    def parse_book(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "description": response.css(".product_page p::text")[10].get(),
        }
    
    def parse_quote(self, response):
        for quote in response.css("div.quote"):
            yield {
                "quote": quote.css("span.text::text").extract()
            }
        
        nextPage = response.css("li.next a::attr(href)").get()
        if nextPage is not None:
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback=self.parse_quote)'''