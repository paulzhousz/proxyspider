#!/usr/bin/python
# -*- coding:utf-8 -*-
# ====================================================================
# Project: 'proxyspider'
# File: 'xicidailispider.py'
# Description:
#    desc
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time: '2016-06-21 13:39'
# Update Log:
#  1.
#  2.
# =====================================================================
import scrapy
from scrapy import Spider
from proxyspider.items import ProxyServer


class XiciDailiSpider(Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    page_start = 1
    page_end = 11
    start_urls = []

    def __init__(self):
        self.start_urls.extend(
            [u'http://www.xicidaili.com/wn/%s' % num for num in range(self.page_start, self.page_end)])
        self.start_urls.extend(
            [u'http://www.xicidaili.com/nn/%s' % num for num in range(self.page_start, self.page_end)])

    def parse(self, response):
        """
            处理爬取的页面中代理服务器的ip和port，并进行校验，获取有效的代理服务器
            :param response:
            """
        trs = response.xpath('//tr[@class="odd" or @class=""]')
        for tr in trs:
            str_ip = tr.xpath('./td[2]/text()').extract()[0]
            str_port = tr.xpath('./td[3]/text()').extract()[0]
            item = ProxyServer()
            item['proxy_ip'] = str_ip
            item['Proxy_port'] = str_port
            yield item


