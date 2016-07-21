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
from proxyspider.items import ProxyServer
from proxyspider.scrapyutil import ProxyUtil


class ProxySpider(CrawlSpider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = [
        'http://www.xicidaili.com/nn/',
        'http://www.xicidaili.com/wn/',
    ]
    rules = [
        # 抓取1-9页的代理服务器，后面页数不处理
        Rule(LinkExtractor(allow=('nn/\d$')), callback='parse_item'),
        Rule(LinkExtractor(allow=('wn/\d$')), callback='parse_item')
    ]

    def parse_start_url(self, response):
        self.parse_item(response)

    def parse_item(self, response):
        """
        处理爬取的页面中代理服务器的ip和port，并进行校验，获取有效的代理服务器
        :param response:
        """
        trs = response.xpath('//tr[@class="odd" or @class=""]')
        for tr in trs:
            str_ip = tr.xpath('./td[2]/text()').extract()[0]
            str_port = tr.xpath('./td[3]/text()').extract()[0]
            if ProxyUtil.is_valid_proxy(str_ip, str_port):
                item = ProxyServer()
                item['proxy_ip'] = str_ip
                item['proxy_port'] = str_port
                yield item
            else:
                print ('Bad proxy:%s--%s' % (str_ip, str_port))
