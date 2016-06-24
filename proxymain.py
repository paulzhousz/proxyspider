#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################################
# File Name: proxymain.py
# Description: 用于启动proxy scrapy爬虫
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time:2016-05-23 22：26
# Update Log:
#########################################################
import argparse

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from proxyspider.spiders.xicidailispider import XiciDailiSpider

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='crawl proxy server from http://www.xicidaili.com')
    parser.add_argument("-c", "-crawl", nargs="+", help="crawl proxy info. example : python proxymain.py -c 100 200",
                        type=int)
    parser.add_argument("-t", "-test", help="check proxy is available. command : python main.y -t db", )
    args = parser.parse_args()
    if args.c is not None:
        if len(args.c) > 1 and args.c[0] < args.c[1]:
            print ('crawl proxy start...')
            XiciDailiSpider.page_start = args.c[0]
            XiciDailiSpider.page_end = args.c[1]
            process = CrawlerProcess(get_project_settings())
            process.crawl(XiciDailiSpider)
            process.start()
        else:
            print ('invalid parameter!')


# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl xici".split())
