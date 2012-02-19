# encoding:utf-8
# use BeautifulSoup to get font|p context
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
import threading


queue_lock = threading.RLock()
file_lock = threading.RLock()
socket.setdefaulttimeout(8) 

g_url_queue = Queue.Queue()
g_url_queue.put('http://www.bupt.edu.cn/')

g_file_queue = Queue.Queue()
tt = ['http://www.bupt.edu.cn/']
g_url_set = set(tt)
max_deep = 1



#######################################################
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

  
def get_context( soup ,url):       
    allfonttext=soup.findAll(['a','p','font'])
    if len(allfonttext)<=0:
        print 'not found text'
    fwrite = open('u'+str(url) ,'w')
    for i in allfonttext:
        t = (i.renderContents() )
        context = strip_tags(t)
        fwrite.write (context)

    fwrite.close()

        

class get_page_thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name
    
    def run(self):
        global g_url_set
        global g_url_queue
        global g_file_queue

        count = 0
        print 'debug'
        while g_url_queue.empty() is not True:
            print self.t_name

            # 增加一个锁
            queue_lock.acquire()
            l_url = g_url_queue.get()

            queue_lock.release()
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

            file_lock.acquire()
            g_file_queue.put(count+1)
            file_lock.release()
            
            count += 1
            if count >= 100 :
               exit
        
class get_url_list_thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name
        
  

        
    def run(self):
        global g_url_set
        global g_file_queue
        global queue_lock
        global file_lock

        while g_file_queue.empty() is not True:
            file_lock.acquire()
            filename = g_file_queue.get()
            file_lock.release()

            fd = open(str(filename),'r')
            html = fd.read();
            soup = BeautifulSoup(html) 

            get_context(soup,filename)
            
            re_html = r'(http://(\w+\.)+\w+)'        
            res = soup.findAll('a') #找到所有a标签

            
            
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
                    g_url_set |= set('fuxiang')
                    if str_url not in g_url_set :
                        queue_lock.acquire()
                        g_url_queue.put(str_url )
                        queue_lock.release()
                        g_url_set |= set(str_url)
            
# uncomplete
def get_html_page(url):
    furl =  urllib2.urlopen(url)
    html = furl.read()
    soup = BeautifulSoup(html)


if __name__ == "__main__":
    thread1 = get_page_thread('a')
    
    thread2 = get_url_list_thread('b')
    thread3 = get_page_thread('c')
    thread4 = get_page_thread('d')

    thread1.start()
    time.sleep(20)
    thread2.start()

    time.sleep(20)
    thread3.start()
    thread4.start()
    


