# encoding:utf-8
from BeautifulSoup import BeautifulSoup
import sys
from FileProcess import *
from MysqlProcess import *
    
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
    seeds = get_seed_file()
    print seeds
    for url in seeds:
#        print url
        index = get_index_bbs( get_xml(url) )
        #print index
#        store_index()
#        print "最近的热点活动"
#        for ii in index:
#            print 'title :'  ,ii[0]
#            print ii[3]
#            print "\n\n-------------------------------------------------\n\n"
#    
        insert_bbsindex(index)
    
#    show_bbsindex()
    
    
    
if __name__ == "__main__":
#    show_bbsindex()
    
    lookup_main("http://bbs.byr.cn/rss/board-SCS")


