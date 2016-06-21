#!/usr/bin/python
# -*- coding:utf-8 -*-
#########################################################
# File Name: main.py
# Description: 用于启动proxy scrapy爬虫
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time:2016-05-23 22：26
# Update Log:
#########################################################
import argparse

from scrapy import cmdline

cmdline.execute("scrapy crawl xici".split())