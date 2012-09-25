# encoding:utf-8
from BeautifulSoup import BeautifulSoup
import sys
from FileProcess import *
import MysqlProcess2
import MysqlProcess

    
###
"""
[ [title ,link ,author,content ] ]
"""
###
def get_index_bbs(content):
    bbs_index = []
    soup = BeautifulSoup(content)
    items = soup.findAll('item')
    for x in items:
        item = (x)
        title = item.find('title').renderContents()
        
        link = item.find('guid').renderContents()

        author = item.find('author').renderContents()

        if item.find('description'):
            description = item.find('description').renderContents()
        else :
            description = ""

        sub = [title ,link ,author,description]

        bbs_index.append( sub)
    
    return bbs_index

#爬取的入口函数
def crawl_main():
    seeds = get_seed_file()
    db = MysqlProcess2.MysqlProcess()
    for url in seeds:
        index = get_index_bbs( get_xml(url) )
#        insert_bbsindex(index)
        db.insertBbsDb(index)
#        MysqlProcess.insert_bbsindex(index)

    
    
if __name__ == "__main__":
        
    crawl_main()

    print "done it"


