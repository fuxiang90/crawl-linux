#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
#参考http://4nail.iteye.com/blog/848017
import smtplib
from email.mime.text import MIMEText
#############
#要发给谁，这里发给2个人
mailto_list=["fuxiang90@gmail.com"]
#####################
#设置服务器，用户名、口令以及邮箱的后缀
mail_host="smtp.163.com"
mail_user="370386403fx@163.com"
mail_pass="1xiao2go"
mail_postfix="163.com"
######################
def send_mail(to_list,sub,content):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_user
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

def test_send(index):
    content  = " titile : %s \n  link : %s \n author : %s \n content : %s \n\n "
    allcontent = ""
    
    print len(index)
    count = 1
    for i in index:
        temp = content % (str(i[1]) ,str(i[2]), str(i[3]) ,str(i[4])) # 如果加上content i[4] ，说长度不够
        allcontent = allcontent + temp 
    
    print allcontent
    if send_mail(mailto_list,"最近讲座",allcontent):
        print "发送成功"
    else:
        print "发送失败"
    
if __name__ == '__main__':
    index = [ ['test5','test','test','test'],['test4','test','test','test']]
    test_send(index)
    
   
