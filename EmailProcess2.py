import smtplib
from email.mime.text import MIMEText

sender = '370386403fx@163.com'
receiver = ['fuxiang90@gmail.com','f397993401@gmail.com']
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '***'
password = '***'





def sender(index):    
    content  = " titile : %s \n  link : %s \n author : %s \n content : %s \n\n "
    allcontent = ""
    
    for i in index:
        temp = content % (i[0] ,i[1], i[2] ,i[3])
        allcontent = "".join(temp )
    
    print allcontent
    msg = MIMEText(allcontent,'plain','utf-8')

    msg['Subject'] = subject

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('370386403fx@163.com','1xiao2go')
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    index = [ ['test5','test','test','test'],['test4','test','test','test']]
    sender(index)
    
