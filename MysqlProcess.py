# -*- coding: utf-8 -*-
import sys
import MySQLdb


"""
bbsindex -->
    id ,title ,link ,author ,content ,score ,b1 ; b1 
"""
def conn_bbsindex():
    conn = MySQLdb.connect(host = 'localhost',user = 'osqa',passwd = 'osqa' ,db = 'indexdb', charset='utf8')
    return conn

#sql = "insert into bbsindex(title ,link ,content) values(  "


def isin_index(mtitle):
    conn = conn_bbsindex()
    cur = conn.cursor()
    sql = "select title from bbsindex where title = '%s'" %(mtitle)
    cur.execute(sql)
    
    all = cur.fetchall()
    size = len(all)
    for i in all :
        print i
    if size == 0:
        return False
    else :
        return True


def insert_bbsindex(index):
    conn = conn_bbsindex()
    cur = conn.cursor()
    for i in index :
        try :
            if isin_index(i[0]) == True: 
                continue
            sql = "insert into bbsindex(title ,link ,author ,content,score) values('%s' ,'%s' ,'%s' ,'%s', %d)"  %(str(i[0]),str([1]),str(i[2]),str(i[3]),1)
#            sql = "insert into bbsindex(title ,link ,author ,content,score) values('%s' ,'%s' ,'%s' ,'%s', %d)"  %(i[0].decode('utf-8'),i[1].decode('utf-8'),i[2].decode('utf-8'),i[3].decode('utf-8'),1)
            
            #sql = "insert into bbsindex(title ,score) values('%s' ,'%s' ,'%s' ,'%s', %d)"  %(str(i[0]),1)
            print sql
            cur.execute(sql)
            conn.commit()
            print 'insert ok'
        except :
            print 'insert bad'
            conn.rollback()
    conn.commit()
    cur.close()
    conn.close()
    
def show_bbsindex():
    conn = conn_bbsindex()
    cur = conn.cursor()
    cur.execute('select * from bbsindex')
    all = cur.fetchall()
    for i in all :
        for ii in i:
            print ii
    
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

if __name__ == "__main__":
#    index = [ ['test2','test','test','test']]
    index = [ ['test5','test','test','test'],['test4','test','test','test']]
    insert_bbsindex(index)
    show_bbsindex()
        
    
