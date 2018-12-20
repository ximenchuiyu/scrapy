# -*- coding: utf-8 -*-
import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'
    # allowed_domains = ['eeee']

    def start_requests(self):
        while 1:
            yield scrapy.Request('https://www.digikey.com/products/en/sensors-transducers/pressure-sensors-transducers/512/page/39',self.show,dont_filter=True)

    def show(self, response):
        print(len(response.text))
        # print(response.xpath('//*[@id="result"]/div/p[1]/code/text()').extract_first())
