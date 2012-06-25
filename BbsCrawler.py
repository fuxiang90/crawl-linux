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
    items = soup.findAll('item')
    for x in items:
        item = (x)
        title = item.find('title').renderContents()
#        print title
        link = item.find('link').renderContents()
#        print link
        author = item.find('author').renderContents()
#        print author
        description = item.find('description').renderContents()
        description = filter_tags(description)
        print description
        sub = [title ,link ,author,description]

        bbs_index.append( sub)
    
    return bbs_index

def lookup_main(url):
    index = get_index_bbs( get_xml(url) )
    print "最近的热点活动"
#    for ii in index:
#        print 'title :'  ,ii[0]
#        print ii[3]
#        print "\n\n-------------------------------------------------\n\n"
    
    insert_bbsindex(index)
    show_bbsindex()
    
    
    
if __name__ == "__main__":
    lookup_main("http://bbs.byr.cn/rss/board-SCS")
#    lookup_main('http://buptoa.bupt.edu.cn/broad.nsf/depView_qt?OpenView&Start=14&Count=30&Expand=14#14')
#    get_content( get_xml('http://bbs.byr.cn/rss/board-SCS') )

#    print strip_tags(open('1.xml').read() )
#    tt = get_content( test('1.xml'))
#    tt = get_content( get_xml('http://bbs.byr.cn/rss/board-BYR_Bulletin') )
#    fp = open('1.re','w')
#    for tti in tt:
#        for ttii in tti :
#             fp.write( ttii) 
#        
#        print "\n"
#        
#        
#    
#    fp.close()
#    fp.write( (str(tt)).decode('utf-8') )
#    fp.close
#    
#    ttt = open('1.re','r')
#    tttt = ttt.read()
#    print unicode( tttt.decode('utf-8','ignore'))
