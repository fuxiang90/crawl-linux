# encoding:utf-8
import sys
import MySQLdb
import random
import myLog
from FileProcess import *
import time

"""
bbsindex -->
    id ,title ,link ,author ,content ,score ,b1 ; b1 
"""
def conn_bbsindex():
    conn = MySQLdb.connect(host = 'localhost',user = 'osqa',passwd = 'osqa' ,db = 'indexdb', charset='utf8')
    return conn

#sql = "insert into bbsindex(title ,link ,content) values(  "


#现在是使用直接查数据库的方式来判重

def isin_index( text):
    conn = conn_bbsindex()
    cur = conn.cursor()
    sql = "select title from bbsindex where link = '%s'" %(text)
    cur.execute(sql)
    
    all = cur.fetchall()
    size = len(all)
    if size == 0:
        return False
    else :
        return True
# 使用先将链接拷贝出来的方式
def isInIndex(link,linkDict):
    if link in linkDict:
        return True
    return False

def insert_bbsindex(index):
    conn = conn_bbsindex()
    cur = conn.cursor()
    for i in index :
        try :
            if isin_index(i[1]) == True: 
                continue
            randnum = random.randint(2,10)#先生成一个随机数的
            text = filter_tags(str(i[3]))
            sql = "insert into bbsindex(title ,link ,author ,content,text,score,date) values('%s' ,'%s' ,'%s','%s','%s', '%d','%s')"  %(str(i[0]),str(i[1]),str(i[2]),str(i[3]),text,randnum,time.strftime('%Y-%m-%d',time.localtime(time.time())))
#            sql = "insert into bbsindex(title ,link ,author ,content,score,date) values('%s' ,'%s' ,'%s' ,'%s', %d,'%s')"  %(str(i[0]),str(i[1]),str(i[2]),str(i[3]),randnum,time.strftime('%Y-%m-%d',time.localtime(time.time())))

            print 
            cur.execute(sql)
            conn.commit()
        except MySQLdb.ProgrammingError as error:
            myLog.writeLog(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print "---->SQL Error: %s" % error
            myLog.writeLog("---->SQL Error: %s" % error)
            myLog.writeLog( sql)
            myLog.writeLog('--------------------')
            conn.rollback()
    conn.commit()
    cur.close()
    conn.close()

def getLink():
    conn = conn_bbsindex()
    cur = conn.cursor()
    cur.execute('select Id ,link from bbsindex ')
    linkDict = dict()    
    all = cur.fetchall()
    for items in all:
        linkDict[items[1]] = items[0]
    cur.close()
    conn.close()
    return linkDict
    
        
def show_bbsindex():
    conn = conn_bbsindex()
    cur = conn.cursor()
    cur.execute('select * from bbsindex')
    all = cur.fetchall()
    for i in all :
        ans = 0
        for ii in i:
            print ans, ":   " ,ii
            ans = ans + 1
    
    cur.close()
    conn.close()

"""
oacount  取前几个记录
"""
def get_bbsindex( oacount ):
    conn = conn_bbsindex()
    cur = conn.cursor()
    cur.execute('select * from bbsindex  order by score desc ,id desc limit 0,%d' %(oacount) )
    all = cur.fetchall()
    index = []
    for i in all :
        t = []
        for ii in i:
            t.append(ii)
        
        index.append(t)
    
    cur.close()
    conn.close()
    return index

def deleteBbsdb():
    conn = conn_bbsindex()
    cur = conn.cursor()
    cur.execute('delete  from bbsindex where 1 ')
    cur.close()
    conn.close()

def testLink():
    seeds = ["http://bbs.byr.cn/article/Home/46050","http://bbs.byr.cn/article/SCS/142669"]
    for i in range(1,1000):
        for seed in seeds:
            if isin_index(seed):
                print "is in mysql"
def testLink2():
    linkDict = getLink()
    seeds = ["http://bbs.byr.cn/article/Home/46050","http://bbs.byr.cn/article/SCS/142669"]
    for i in range(1,1000):
        for seed in seeds:
            if isInIndex(seed,linkDict):
                print "is in mysql"
    
    
if __name__ == "__main__":
#    index = [ ['test2','test','test','test']]
    index = [ ['test5','test122222233564','test','test']]
    insert_bbsindex(index)
    #show_bbsindex()
    #deleteBbsdb()
#    testLink2()
    print "done it"
        
    
