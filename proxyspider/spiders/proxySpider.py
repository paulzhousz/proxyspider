#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
====================================================================
File Name:proxySpider.py
Description:
    爬虫主程序，抓取www.xicidaili.com中代理列表
Author: Paul Zhou(paulzhousz@gmail.com)
Created Time: 2016-5-25 17:00
Update Log:
  1.
  2.
=====================================================================
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ProxySpider(CrawlSpider):
    name = 'xicidaili'
    allowed_domains = 'www.xicidaili.com/'
    start_urls = [
        'http://www.xicidaili.com/nn/1',
        # 'http://www.xicidaili.com/wn/1'
    ]
    rules = [
        Rule(LinkExtractor(allow=(r'nn/\[1-9]')), callback='parse_Item', follow=False),
        # Rule(LinkExtractor(allow=(r'wn/\d')),callback='parse_Item',follow=False)
    ]

    def parse_start_url(self, response):
        print 'url=' + response.url

    def parse_Item(self, response):
        print 'url=' + response.url
        # pass
