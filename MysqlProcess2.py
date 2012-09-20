# encoding:utf-8
import sys
import MySQLdb
import random
import myLog
from FileProcess import *
import time

class MysqlProcess(object):
    def __init__ (self):
        self.linkDict = self.getLink()
        self.conn = self.connConnect()
    def connConnect(self,dbstr = "indexdb",hoststr = "localhost",userstr = "osqa",passwdstr = "osqa"):
        conn = MySQLdb.connect(host = str(hoststr),user = str(userstr),passwd = str(passwdstr) ,db = str(dbstr), charset='utf8')
        return conn
    def isInIndex(self,link):
        if link in self.linkDict:
            return True
        return False
    def getLink(self):
        self.conn = self.connConnect()
        cur = self.conn.cursor()
        cur.execute('select Id ,link from bbsindex ')
        linkDict = {}
        all = cur.fetchall()
        for items in all:
            linkDict[items[1]] = items[0]
        cur.close()
        self.conn.close()
        return linkDict

    def insertBbsDb(self,index):
#        self.conn = self.connConnect(self)
        cur = self.conn.cursor()
        for i in index :
            try :
                if self.isInIndex(i[1]) == True: 
                    continue
                randnum = random.randint(2,10)#先生成一个随机数的
                sql = "insert into bbsindex(title ,link ,author ,content,text,score,date) values('%s' ,'%s' ,'%s' ,'%s',%s', %d,'%s')"  %(str(i[0]),str(i[1]),str(i[2]),str(i[3]),filter_tags(str(i[3])),randnum,time.strftime('%Y-%m-%d',time.localtime(time.time())))
                cur.execute(sql)
                self.conn.commit()
            except :
                myLog.writeLog(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                myLog.writeLog('insert bad ')
                myLog.writeLog(i[3])
                myLog.writeLog('--------------------')
                self.conn.rollback()
            self.conn.commit()
        
        cur.close()

    def showDb(self):
        self.conn = self.connConnect()
        cur = self.conn.cursor()
        cur.execute('select * from bbsindex')
        all = cur.fetchall()
        for i in all :
            ans = 0
            for ii in i:
                print ans, ":   " ,ii
                ans = ans + 1
    
        cur.close()
        self.conn.close()

    
    
if __name__ == "__main__":
#    index = [ ['test2','test','test','test']]
    index = [ ['test5','test7','test','test'],['test4','test8','test','test']]
    db = MysqlProcess()
    db.insertBbsDb(index)
    
    print "done it"
        
    
