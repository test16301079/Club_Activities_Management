import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import threading
from django.core.mail import *
    
def mail(my_receiver,mail_content):

    send_mail('社团活动管理系统', mail_content, '948525147@qq.com',
              [my_receiver], fail_silently=False)






# def test(my_receiver,mail_content):
#     sender_name = '合同管理系统'
#     receiver_name = '尊敬的用户'
#     theme = '合同管理系统温馨提示'
#
#     my_sender='185873016@qq.com'    # 发件人邮箱账号
#     my_pass = 'wpibkvwjtfohbiab'              # 发件人邮箱密码(当时申请smtp给的口令)
#     ret=True
#     try:
#         msg=MIMEText(mail_content,'plain','utf-8')
#         msg['From']=formataddr([sender_name,my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To']=formataddr([receiver_name,my_receiver])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject']=theme               # 邮件的主题，也可以说是标题
#
#         server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender,[my_receiver,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()# 关闭连接
#     except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret=False