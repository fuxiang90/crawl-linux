from BeautifulSoup import BeautifulSoup          # For processing HTML
import urllib2
import os
import sys
import re
import Queue
import socket
import time

fp = open('1','r')
ff = fp.read()
soup = BeautifulSoup(ff)
res = soup.findAll('a)

res = soup.findAll('a')
re_html = r'(/broad.nsf/(\w+\.)+\?\w+)'


for x in res:
    t = unicode(x)
    m = re.findall(re_html,t)
    for xx in m:
            print xx

