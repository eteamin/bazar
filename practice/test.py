# -*- coding: utf-8 -*-
import smtplib
from datetime import date
from email.mime.text import MIMEText


class SMTPClient(object):
    def __init__(self, subscriber, description):
        self.subscriber = subscriber
        self.description = description
        self.mail_host = 'smtp.mail.yahoo.com'
        self.mail_port = '587'
        self.username = 'eteamin'
        self.password = '123456789Io'
        self.mail_sender = 'eteamin@yahoo.com'
        self.mail_receiver = 'aminetesamian1371@gmail.com'
        self.smtp_client = smtplib.SMTP(self.mail_host, self.mail_port)
        self.smtp_client.ehlo_or_helo_if_needed()
        self.smtp_client.starttls()
        self.smtp_client.login(self.username, self.password)

    def make_mail(self):
        body = 'کاربر:%s \n تاریخ:%s \n دیدگاه: %s' % (self.subscriber, str(date.today()), self.description)
        message = MIMEText(body)
        message['From'] = self.mail_sender
        message['To'] = self.mail_receiver
        message['Subject'] = 't-w-a Feedback'
        return message.as_string()

    def send_mail(self):
        self.smtp_client.sendmail(self.mail_sender, self.mail_receiver, self.make_mail())
        self.smtp_client.quit()

if __name__ == '__main__':
    sda = SMTPClient('asdas', 'sdfsdfs')
    sda.send_mail()