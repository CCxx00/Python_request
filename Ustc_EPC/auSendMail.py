import smtplib
from email.mime.text import MIMEText
from email.header import Header

class mail(object):
    def __init__(self,mail_user,mail_pass,receivers,mail_host="smtp.qq.com",port=25):
        # 第三方 SMTP 服务
        self.mail_host=mail_host#"smtp.qq.com"  #设置服务器
        self.port=port #设置服务器端口号
        self.mail_user=mail_user#"1375062160@qq.com"    #用户名
        self.mail_pass=mail_pass#"covpapiglbgmhdah"   #口令
        self.sender = mail_user
        self.receivers = receivers#['llmxdxcb@gmail.com',]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def message_set(self,msg_mimetext,msg_from,msg_to,msg_subject='DRAMA'):
        self.message = MIMEText(msg_mimetext, 'plain', 'utf-8')
        self.message['From'] = Header(msg_from, 'utf-8')
        self.message['To'] =  Header(msg_to, 'utf-8')
        self.message['Subject'] = Header(msg_subject, 'utf-8')

    def send_mail(self):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, self.port)    # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user,self.mail_pass)
            smtpObj.sendmail(self.sender,self.receivers,self.message.as_string())
            print("邮件发送成功")
        except Exception:
            print("Error: 无法发送邮件")
