#encoding=utf-8 
from BeautifulSoup import BeautifulSoup
import sys
from FileProcess import *
from MysqlProcess import *
from Option import *

def get_all_links_soup(html):
    oa_index = []
    links = []
    re_html = r'a(\w+)'
    
    soup = BeautifulSoup(html)
    res = soup.findAll('a') 
    
#    print res
    for x in res:
        t = unicode(x) 
        title= x.renderContents()
        
        
#        if title.find('()'):
#            title = title[:title.find('()')]
        link = get_link_soup(t)
        link = 'http://buptoa.bupt.edu.cn' + link
        author = u'xueshuban'
        
        description = filter_tags(get_page(link))
        if description is None:
            continue
        
        sub = [title ,link ,author,description]
        oa_index.append(sub)
    
    return oa_index


           
def get_link_soup(page):


    start_link = page.find('<a href=')
    start_pos = page.find('"',start_link)
    end_pos = page.find('"',start_pos+1)
    url = page[start_pos+1:end_pos]
    
    # print end_pos , len(page) -1
    return url

 
def get_buptoa_page(url):
    return get_page(url)

    

 
def test_main(url):
#    html = get_buptoa_html(url)
    html = test_utf('2.htm')
#    print html
#    print html.lower()
    index = get_all_links_soup(html.lower())
#    for ii in index:
#        print 'title :'  ,ii[0]
#        print "---------------------------------------------------"
#        print len(ii[3])
#        print ii[3]
#        print "---------------------------------------------------"
#    store_index(index,'buptoa_index')
#    print index
    insert_bbsindex(index)
    show_bbsindex()
    
    
def lookup_main(url):
    
    index = filter_tags( get_buptoa_html(url) )
    print index
    
    
    
if __name__ == "__main__":
    test_main('http://buptoa.bupt.edu.cn/broad.nsf/depView_qt?OpenView&Start=14&Count=30&Expand=14#14')
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
