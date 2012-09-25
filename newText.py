# encoding:utf-8
import sys
import MySQLdb
import random
from FileProcess import *
from MysqlProcess import *

def ExtraContent():
    conn = conn_bbsindex()
    cur = conn.cursor()
    sql = "select id,content,text from bbsindex " 
    cur.execute(sql)
    all = cur.fetchall()
    size = len(all)
    
    for item in all:
        if item[2] == '':
            s = "update  bbsindex set text = '%s' where id = '%d'"  %(filter_tags(item[1]),int(item[0]))
            cur.execute(s)
            conn.commit()

if __name__ == "__main__":
    ExtraContent()
    