import scrapy


class SnpSpider(scrapy.Spider):
    name = "snp"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        number = response.xpath('//table[@class="table table-hover table-borderless table-sm"]//td[1]/text()').get()
        company = response.xpath('//table[@class="table table-hover table-borderless table-sm"]//td[2]/a/text()').get()
        symbol = response.xpath('//table[@class="table table-hover table-borderless table-sm"]//td[3]/a/text()').get()
        ytd_return = response.xpath('//table[@class="table table-hover table-borderless table-sm"]//td[4]/text()').get()
        return {"number": number, "company": company, "symbol": symbol,
                "ytd_return": ytd_return}