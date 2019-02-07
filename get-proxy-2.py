#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
import random
from BeautifulSoup import BeautifulSoup
import socket
socket.setdefaulttimeout(2)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# http://www.xicidaili.com/
# 这个网址的代理好用，50%以上的可用性，不用测试

url = 'http://www.xicidaili.com/nn/%s/'

def findProxy():
    proxys = []
    print '开始从%s上查找代理' % url
    for i in range(1,10):
        tmp = spider_xicidaili(i)
        proxys += tmp
    writeFile(proxys)
    print '共找到%s个代理' % len(proxys)

def spider_xicidaili(index):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib2.build_opener()
    opener.addheaders = [headers]
    try:
        urls = []
        page = opener.open(url % index).read()
        page = BeautifulSoup(page)
        proxys = page.table.findAll('tr')
        for p in proxys:
            if p.findAll('th'):
                continue;
            else:
                td = p.findAll('td')
            host, port = td[1].string, td[2].string
            print host, port
            urls.append('http://%s:%s/' % (host, port))
        return urls
    except Exception, e:
        print e
        return []

def writeFile(proxys):
    with open('result.txt', 'w') as f:
        for p in proxys:
            f.write(str(p) + '\n')

def testIP(url):
    pro = urllib2.ProxyHandler({'http': url})
    opener = urllib2.build_opener(pro, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    try:
        content = urllib2.urlopen('http://www.baidu.com').read()
        return True
    except Exception, e:
        print e
        return False
    return False

def test_spider_xicidaili():
    spider_xicidaili(1)

if __name__ == "__main__":
    #test_spider_xicidaili()
    findProxy()
