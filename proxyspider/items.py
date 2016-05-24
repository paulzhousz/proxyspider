#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################################
# File Name: items.py
# Description: proxy scrapy item 定义
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time:2016-05-24 17:50
# Update Log:
#########################################################
import scrapy


class ProxyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    proxy_ip=scrapy.Field()
    Proxy_port=scrapy.Field()
    proxy_type=scrapy.Field()
    proxy_location=scrapy.Field()
    proxy_source=scrapy.Field()

