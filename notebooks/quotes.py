import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
            'http://quotes.toscrape.com/tag/humor/page/1/',
            'http://quotes.toscrape.com/tag/humor/page/2/',
        ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }