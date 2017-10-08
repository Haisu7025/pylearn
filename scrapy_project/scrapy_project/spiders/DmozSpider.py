import scrapy
from scrapy import Item, Field


class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            dmoz_item = DmozItem()
            dmoz_item['title'] = sel.xpath('a/text()').extract()
            dmoz_item['link'] = sel.xpath('a/@href').extract()
            dmoz_item['desc'] = sel.xpath('text()').extract()
            print "================================================"
            print dmoz_item
            print "================================================"
