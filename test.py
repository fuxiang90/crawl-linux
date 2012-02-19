from BeautifulSoup import BeautifulSoup          # For processing HTML
import urllib2
import os
import sys
import re
import Queue
import socket
import time

fp = open('1' ,'r')
context = fp.read()

t = set('z')
for i in context:
    print 'now is ' + i
    if i  in t:
        print i + 'in'
    else:
        print 'not in'
        t |= set(i)
    print t
    print '################'
