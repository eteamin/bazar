# -*- coding: utf-8 -*-
import smtplib
from tg import config as tg_config
from datetime import date
from email.mime.text import MIMEText


class FeedbackSMTPClient(object):
    def __init__(self, name, last_name, email, description):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.description = description
        self.mail_host = tg_config.get('feedback.smtp_server.host')
        self.mail_port = tg_config.get('feedback.smtp_server.port')
        self.username = tg_config.get('feedback.smtp_username')
        self.password = tg_config.get('feedback.smtp_password')
        self.mail_sender = tg_config.get('feedback.from_address')
        self.mail_receiver = tg_config.get('feedback.receiver')
        self.smtp_client = smtplib.SMTP(self.mail_host, self.mail_port)
        self.smtp_client.ehlo_or_helo_if_needed()
        self.smtp_client.starttls()
        self.smtp_client.login(self.username, self.password)

    def make_mail(self):
        body = u'کاربر %s %s به آدرس ایمیل %s در تاریخ %s نوشته است: \n%s' % (
            self.name,
            self.last_name,
            self.email,
            date.today(),
            self.description
        )
        message = MIMEText(body, _charset='utf-8')
        message['From'] = self.mail_sender
        message['To'] = self.mail_receiver
        message['Subject'] = u'بازخورد جدید از کاربران سایت فدراسیون وزنه برداری'
        return message.as_string()

    def send_mail(self):
        self.smtp_client.sendmail(self.mail_sender, self.mail_receiver, self.make_mail())
        self.smtp_client.quit()
