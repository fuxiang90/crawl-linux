import sys
import re
import socket
import time

socket.setdefaulttimeout(8) 
##page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'

# find all url in a webpage 
import urllib2

count = 1
def store_page(page):
    chdir("C:\Users\Administrator\workspace\python\search\file")
    fwrite = open (str(count),'w')
    fwrite.write(page.read())
    fwrite.close()
def get_page(url):
    try :
        import urllib2
        page = urllib2.urlopen(url)
        return page.read()
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
##        print url
        if url not in crawled:
            content = get_page(url)
            
            temp = get_all_links(content)
            union(next_deep, temp)
            crawled.append(url)
        if not tocrawl:
                tocrawl,next_deep = next_deep,[]
                deep = deep + 1
    return crawled
    
if __name__ == "__main__":

##    print get_all_links( get_page("http://www.bupt.edu.cn") )
    crawl_web("http://www.bupt.edu.cn",1)

    
    
