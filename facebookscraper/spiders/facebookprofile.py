import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FacebookprofileSpider(CrawlSpider):
    name = 'facebookprofile'
    allowed_domains = ['facebook.com']
    start_urls = ['https://www.facebook.com/pg/{username}/community/?ref=page_internal']
    HEADERS = {
                'Accept-language': 'en\r\n',
                'Cookie': 'foo=bar\r\n',
                'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:10\r\n' 
               }
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], self.parse_item)

    def parse_item(self, response):
        item = {}
        print('start=================================')
        print(response)
        print('end=================================')
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
