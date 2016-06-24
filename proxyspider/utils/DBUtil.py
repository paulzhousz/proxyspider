#!/usr/bin/python
# -*- coding:utf-8 -*-
# ====================================================================
# Project: 'proxyspider'
# File: 'DBUtil.py'
# Description:
#    数据库相关工具类
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time: '2016-06-24 14:54'
# Update Log:
#  1.
#  2.
# =====================================================================

import pymongo

from proxyspider.items import ProxyServer
from proxyspider.settings import MONGO_DATABASE, MONGO_URI


class DBUtil(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DATABASE]
        self.proxies = self.db[ProxyServer.__name__]

    def update_seq(self):
        """
        更新proxy sequence ID
        """
        proxy_seq = 1

        proxylist = self.proxies.find()
        for proxy in proxylist:
            proxy_ip = proxy['proxy_ip']
            proxy_port = proxy['Proxy_port']
            self.proxies.update({
                                    'proxy_ip': proxy_ip,
                                    'Proxy_port': proxy_port},
                                {'$set': {'proxy_seq': proxy_seq}})
            proxy_seq += 1
        self.client.close()
