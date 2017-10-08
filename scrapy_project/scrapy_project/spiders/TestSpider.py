#!/usr/bin/python
# -*- coding: UTF-8 -*-

from scrapy import Spider
from scrapy import Request


class TestSpider(Spider):
    name = 'test'
    start_urls = [
        "http://www.qq.com/",
    ]

    def login_parse(self, response):
        ''' 如果登录成功,手动构造请求Request迭代返回 '''
        print response
        for i in range(0, 10):
            yield Request('http://www.example.com/list/1?page={0}'.format(i))

    def start_requests(self):
        ''' 覆盖默认的方法(忽略start_urls),返回登录请求页,制定处理函数为login_parse '''
        return Request('http://www.example.com/login', method="POST", body='username=bomo&pwd=123456', callback=self.login_parse)

    def parse(self, response):
        ''' 默认请求处理函数 '''
        print response
