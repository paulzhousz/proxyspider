#!/usr/bin/python
# -*- coding:utf-8 -*-
# ====================================================================
# Project: 'proxyspider'
# File: 'ProxyUtil.py'
# Description:
#    代理服务器相关工具类
# Author: Paul Zhou(paulzhousz@gmail.com)
# Created Time: '2016-06-24 15:16'
# Update Log:
#  1.
#  2.
# =====================================================================
import urllib
import socket
import time

from threading import Thread
from .DBUtil import DBUtil



class DetectProxy(Thread):
    '''
    检测代理的可用性
    '''
    url = 'http://ip.chinaz.com/getip.aspx'

    def __init__(self, p_part, p_sum):
        Thread.__init__(self)
        self.part = p_part  # 检测的分区
        self.sum = p_sum  # 检索的总区域
        socket.setdefaulttimeout(2)

        self.dbutil = DBUtil()
        self.counts = self.dbutil.proxies.count()

    def run(self):
        self.detect()  # 开始检测
        self.dbutil.closedb()

    def detect(self):
        '''

        :return:
        '''
        if self.counts < self.sum:
            return

        pre = self.counts / self.sum
        start = pre * (self.part - 1)
        end = pre * self.part
        # 如果是最后一部分，结束就是末尾
        if self.part == self.sum:
            end = self.counts

        # 大于start小于等于end
        part_proxies = self.dbutil.proxies.find({'proxy_seq': {'$gt': start, '$lte': end}})

        for proxy in part_proxies:
            proxy_ip = proxy["proxy_ip"]
            proxy_port = proxy["Proxy_port"]

            try:
                proxy_host = "http://user:pwd@" + proxy_ip + ":" + proxy_port
                response = urllib.urlopen(self.url, proxies={"http": proxy_host})

                if response.getcode() != 200:
                    self.dbutil.proxies.remove({'proxy_ip': proxy_ip, 'proxy_port': proxy_port})
            except Exception, e:
                self.dbutil.proxies.remove({'proxy_ip': proxy_ip, 'proxy_port': proxy_port})
                continue


class DetectManager(Thread):
    def __init__(self, threadSum):
        Thread.__init__(self)
        self.dbutil = DBUtil()
        self.dbutil.update_seq()
        self.pool = []
        for i in range(threadSum):
            self.pool.append(DetectProxy(i + 1, threadSum))

    def run(self):
        self.startManager()
        self.checkState()
        self.dbutil.closedb()

    def startManager(self):
        for thread in self.pool:
            thread.start()

    def checkState(self):
        now = 0
        while now < len(self.pool):
            for thread in self.pool:
                if thread.isAlive():
                    now = 0
                    break;
                else:
                    now += 1
            time.sleep(0.1)

        self.dbutil.update_seq()