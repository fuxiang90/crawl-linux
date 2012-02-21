# encoding:utf-8
# use BeautifulSoup to get font|p context
# 单线程版本的爬取html ，并深度遍历 ，之后 抽取正文 ，但是单线程未免有点慢
# 可以随意的使用这段代码，但请保留 下面的一行
# author ： fuxiang ，mail： fuxiang90@gmail.com
from BeautifulSoup import BeautifulSoup          # For processing HTML
import urllib2
import os
import sys
import re
import Queue
import socket
import time

socket.setdefaulttimeout(5) 

g_url_queue = Queue.Queue()
g_url_queue.put('http://www.bupt.edu.cn/')
tt = ['http://www.bupt.edu.cn/']
g_url_set = set(tt)
max_deep = 1

#  传入的参数是soup 类型 这个提取soup 类型里面的网址
def get_url_list(html):
    global g_url_set
    re_html = r'(http://(\w+\.)+\w+)'
    
    res = html.findAll('a') #找到所有a标签
    
    for x in res:
        t = unicode(x) #这里的x是soup对象
        #url[pos] = str(unicode(x['href']) )
        #t = unicode(x)
        #print unicode(x['href'])
        m = re.findall(re_html , t)
        if m  is None:
            continue
        for xx in m:            
            str_url = xx[0]
            #print str_url
            if str_url not in g_url_set :
                #print str_url + 'add'
                g_url_queue.put(str_url ) 
                g_url_set |= set([str_url]) #之前是 set(str_url) 这样的url set 出来是一个个字符
            

########################################################
def strip_tags(html):
    """
    Python中过滤HTML标签的函数
    >>> str_text=strip_tags("<font color=red>hello</font>")
    >>> print str_text
    hello
    """
    from HTMLParser import HTMLParser
    html = html.strip()
    html = html.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    return ''.join(result)

#######################################################
# 可以传入 网址 或者 本地文件 ，解析出里面的正文
def get_context( url ):
    re_html = 'http[s]?://[A-Za-z0-9]+.[A-Za-z0-9]+.[A-Za-z0-9]+$'

    m = re.match(re_html,str(url))
    if m is None :   # 如果url 是本地文件
        fp = open(unicode(url),'r') 
    else:
        fp = urllib2.urlopen(url)
    html = fp.read()
    soup = BeautifulSoup(html)
    allfonttext=soup.findAll(['a','p','font'])
    if len(allfonttext)<=0:
        print 'not found text'
    fwrite = open('u'+str(url) ,'w')
    for i in allfonttext:
        t = (i.renderContents() )
        context = strip_tags(t)
        fwrite.write (context)

    fwrite.close()

#######################################################
        
def main_fun(deep):
    global g_url_set
    global g_url_queue
    
    if deep > max_deep:
        return
    count = 0
    print 'debug'
    while g_url_queue.empty() is not True:
        #print 'debug2'
        l_url = g_url_queue.get()
        print l_url
        # 捕捉超时错误 ，有些网页链接不上
        try:
            fp = urllib2.urlopen(l_url)
        except :
            continue
        html = fp.read()
        
        fwrite = open(str(count+1) ,'w')
        fwrite.write(html)
        fwrite.close()
        
        soup = BeautifulSoup(html)
        #print 'debug' + ' ' + str(count+1)
        get_url_list(soup)

        get_context(count+1)
        count += 1
        if count >= 100 :
           return
        
           
    

# uncomplete
def get_html_page(url):
    furl =  urllib2.urlopen(url)
    html = furl.read()
    soup = BeautifulSoup(html)


if __name__ == "__main__":
    main_fun(1)

    time.sleep(10)
    


