import scrapy
from stocks.items import StocksItem


class SnpLoopSpider(scrapy.Spider):
    name = "snp_loop"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        stock = StocksItem()
        rows = response.xpath('//*[@class="table table-hover table-borderless table-sm"]/tbody/tr')
        for row in rows:
            stock['number'] = row.xpath('td[1]/text()').get()
            stock['company'] = row.xpath('td[2]/a/text()').get()
            stock['symbol'] = row.xpath('td[3]/a/text()').get()
            stock['ytd_return'] = row.xpath('td[4]/text()').get()
            yield stock
