# encoding:utf-8
from BeautifulSoup import BeautifulSoup
import sys
from FileProcess import *
from MysqlProcess import *
import time 
import os 
###
"""
[ [title ,link ,author,content ] ]
"""
###
def get_index_bbs(content):
    bbs_index = []
    soup = BeautifulSoup(content)
#    print soup
    items = soup.findAll('item')
    for x in items:
        item = (x)
        title = item.find('title').renderContents()
#        print title
        link = item.find('guid').renderContents()
#        print link
        author = item.find('author').renderContents()
#        print author
        if item.find('description'):
            description = item.find('description').renderContents()
#            description = filter_tags(description)
        else :
            description = ""
#        print description
        sub = [title ,link ,author,description]

        bbs_index.append( sub)
    
    return bbs_index

def lookup_main(url):
  
    os.chdir(r'/home/fuxiang/python/crawl-linux/file')
    fin = open('topten','a+')
   
    index = get_index_bbs( get_xml(url) )
        
    fin.write('------------------------------------------------')
    fin.write('\n')
    fin.write( time.strftime('%Y-%m-%d',time.localtime(time.time())) )
    fin.write('\n')
    for item in index:
        
        fin.write(item[1] )
        fin.write('\n')
    
    fin.close()
        

    

    
    
if __name__ == "__main__":
#    show_bbsindex()
    
    lookup_main("http://bbs.byr.cn/rss/topten")


