# -*- coding: utf-8 -*-
from proxy_ip.IP import get_source
# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
from scrapy import signals
import requests
import redis
# def get_ip_port():
#     url = 'http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=e3aa18236e7d43f08d3c5fb8b7c43452&count=1&expiryDate=0&format=1&newLine=2'
#     response = requests.get(url)
#     proxies = {}
#     ip_port = response.json()['msg'][0]['ip']+":"+response.json()['msg'][0]['port']
#     return ip_port


r = redis.Redis(host='127.0.0.1', port=6379, db=3)
def get_ip_port(type):
    ip = r.rpop('the_ip').decode('utf8')
    last_ip = type+'://' + ip
    return last_ip

def insert_ip(ip):
    the_ip = ip.split('/')[-1]
    print(99999999999,the_ip)
    r.lpush('the_ip', the_ip)


# ip = get_ip_port()
# print(ip)
class IppDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    # def process_request(self, request, spider):
    #     request.meta['download_timeout'] = 10

        # request.meta['proxy'] = 'http://' + '180.104.63.204:28995'

    def process_response(self,request,response,spider):
        print(response.status)
        if response.status >= 400:
            print(2222222222222222222222)
            # ip = get_ip_port()
            # print(ip)
            request.meta['proxy'] =  get_ip_port('https')
            request.meta['download_timeout'] = 10
            return request
        else:
            if len(response.text) >10000:
                print(3333333333333333)
                try:
                    ip = request.meta['proxy']
                    print('存入',ip)
                    insert_ip(ip)
                except:
                    print('成功请求但无代理IP')

                return response
            else:
                print(44444444444444444444)
                # ip = get_ip_port()
                # print(ip)
                # request.meta['proxy'] = 'http://' + ip

                request.meta['proxy'] = get_ip_port('https')
                request.meta['download_timeout'] = 10
                print(0000000000000, request.meta['proxy'])
                return request

    def process_exception(self,request, exception, spider):
        print(1231111111111111111111111111111111111111111111111111111)
        # ip = get_ip_port()
        # print(ip)
        request.meta['proxy'] =  get_ip_port('https')
        request.meta['download_timeout'] = 10
        return request


#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class IppDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
