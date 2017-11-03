# -*- coding: utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# =================定义发送邮件=================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header(u"自动化测试报告",'utf-8')
    msg['From'] = "evandunonline@163.com"
    msg['To'] = "evanzhou@epoque.shoes"
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login("evandunonline@163.com",'')
    smtp.sendmail("evandunonline@163.com","evanzhou@epoque.shoes",msg.as_string())
    smtp.quit()
    print ('Email has send out !')

# =================查找测试报告目录，找到最新生成的测试报告文件=================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print (file_new)
    return file_new

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = str(os.path.normpath(os.path.join(os.path.dirname(__file__),'report'))) + '\\' + now + '-result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"意礴后台自动化测试报告",
                            description=u"环境:windows 10 浏览器:chrome")
    discover = unittest.defaultTestLoader.discover(str(os.path.normpath(os.path.join(os.path.dirname(__file__),'test_case')))+'\\',pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report(str(os.path.normpath(os.path.join(os.path.dirname(__file__),'report')))+'\\')
    #send_mail(file_path)
