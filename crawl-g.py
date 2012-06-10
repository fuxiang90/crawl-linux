import sys
import re

import socket
import time

from FileProcess import *

socket.setdefaulttimeout(8) 
t_page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'

# find all url in a webpage 
import urllib2
        
def get_page(url):
    try :
        import urllib2
        content = urllib2.urlopen(url).read()
        gbk_content = content.decode('gbk')
        utf_content = gbk_content.encode('utf-8')
        return utf_content
    except:
        return ""
def get_url(page):
    
    end_pos = 0
    while end_pos <= len(page) -1:
        start_link = page.find('<a href=')
        start_pos = page.find('"',start_link)
        end_pos = page.find('"',start_pos+1)
        url = page[start_pos+1:end_pos]
        
        # print end_pos , len(page) -1
        if url :
            print url
        else:
            break
        page = page[end_pos:]

def lookup(index,keyword):
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):

    links= []
    end_pos = 0
    while end_pos <= len(page) -1:
        start_link = page.find('<a href=')
        start_pos = page.find('"',start_link)
        end_pos = page.find('"',start_pos+1)
        url = page[start_pos+1:end_pos]
        
        # print end_pos , len(page) -1
        if url :
            links.append(url)
        else:
            break
        page = page[end_pos:]

    return links

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    keywords = content.split()
    for keyword in keywords:
        add_to_index(index,keyword,url)
#def crawl_web(seed):
#        tocrawl = [seed]
#        crawled = []
#        while tocrawl:
#                page = tocrawl.pop()
#                if page not in crawled:
#                        tocrawl = get_all_links
def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    next_deep = []
    deep = 0
    index = []
    while tocrawl and deep <= max_depth:
        url = tocrawl.pop()
        print url
        if url not in crawled:
            content = get_page(url)
            add_page_to_index(index,url,content)
            store_page(content)

            temp = get_all_links(content)
            union(next_deep, temp)
            crawled.append(url)
        if not tocrawl:
                tocrawl,next_deep = next_deep,[]
                deep = deep + 1

    store_index(index)    
    return crawled
    
if __name__ == "__main__":

    print get_all_links( get_page("http://buptoa.bupt.edu.cn/broad.nsf/depView_qt?OpenView&Start=14&Count=30&Expand=14#14") )
#    print filter_tags (get_page("http://buptoa.bupt.edu.cn/broad.nsf/depView_qt?OpenView&Start=14&Count=30&Expand=14#14") )
#    crawl_web("http://bbs.byr.cn",1)
##    store_page(t_page)
    
    
