# -*- coding: utf-8 -*-
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mail():
    def __init__(self, sender_email, sender_password, 
                 port = 587, smtp_server = "smtp.gmail.com"):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.port = port
        self.smtp_server = smtp_server
    def send_email(self, receiver_email, subject, msg, msg_type ='plain'):
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(msg, _subtype=msg_type))
        
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, message.as_string())
            server.quit()
