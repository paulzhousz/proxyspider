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
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='crawl proxy server from http://www.xicidaili.com')
    parser.add_argument("-c", "-crawl", nargs="+", help="crawl proxy info. example : python proxymain.py -c 100 200",
                        type=int)
    parser.add_argument()



# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl xici".split())
