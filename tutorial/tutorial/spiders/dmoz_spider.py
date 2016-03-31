from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dytt8"
    allowed_domains = ["dytt8.net"]
    start_urls = [
     #   "http://www.ygdy8.net/html/gndy/oumei/index.html",
        "http://www.ygdy8.net/html/gndy/china/index.html"
    ]

    # def parse(self, response):
    #     sel = Selector(response)
    #     sites = sel.xpath('//td/b')
    #     items = []
    #     for site in sites:
    #         item = DmozItem()
    #         item['title'] = site.xpath('a/text()').extract()
    #         item['link'] = site.xpath('a/@href').extract()
    #         item['desc'] = site.xpath('text()').extract()
    #         items.append(item)
    #     return items
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//td/b')
        content = sel.xpath('//tr/td')
        for site in sites:
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('text()').extract()
            print u'%s'%desc