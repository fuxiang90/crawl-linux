#!/usr/bin/env python
#encoding=utf-8 

from MysqlProcess import *
from EmailProcess import *


def push():
    index = get_bbsindex(5)
    
#    print index
    test_send(index)
    

if __name__ == '__main__':
    push()
    