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
from proxyspider.utils.DBUtil import DBUtil

from threading import Thread


class Detect_Proxy(Thread):
    url = 'http://ip.chinaz.com/getip.aspx'

    def __init__(self, part, sum):
        Thread.__init__(self)
        self.part = part  # 检测的分区
        self.sum = sum  # 检索的总区域
        dbutil = DBUtil()
        self.counts = dbutil.proxies.count()
