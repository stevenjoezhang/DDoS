#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import socket
import random
from BeautifulSoup import BeautifulSoup
socket.setdefaulttimeout(2)
import sys

headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
opener = urllib2.build_opener()
opener.addheaders = [headers]
url = 'http://www.xicidaili.com/nn/%s/'
index = 1
page = opener.open(url % index).read()
page = BeautifulSoup(page)
#print page
proxys = page.table.findAll('tr')[1].findAll('td')[1].string
print proxys