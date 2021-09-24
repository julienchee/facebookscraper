import scrapy

class Facebooklikecount(scrapy.Spider):
    name = 'facebooklikecount'
    allowed_domains = ['facebook.com']
    start_urls = ["https://graph.facebook.com/{username}?access_token={access_token}&fields=likes"]

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0].format(username=self.username, access_token=self.access_token), self.parse)

    def parse(self, response):
        print('start=================================')
        print(response)
        print('end=================================')
        