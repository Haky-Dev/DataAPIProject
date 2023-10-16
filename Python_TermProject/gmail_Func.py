# -*- coding: utf-8 -*-

import mimetypes
import mysmtplib

from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "logo.html"


class Mail_Service:
    def __init__(self):
        #메일 보내는 사람 주소
        self.senderAddr = "hto52529@gmail.com"     # 보내는 사람 email 주소.
        self.recipientAddr = "" # 받는 사람 
        self.send_massage = ""
        self.massage_contents = ""
        pass
    
    
    def send_to_massage(self, recipient_email = "dnflswldud@gmail.com", send_massage = "str_title", contents = "str_contents"):
        global host
        global port
        global htmlFileName


        #값을 받아옴
        self.recipientAddr = recipient_email
        self.send_massage = send_massage
        self.massage_contents = contents

        #msg = MIMEBase("multipart", "alternative")
        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = self.send_massage
        msg['From'] = self.senderAddr
        msg['To'] = self.recipientAddr

        # MIME 문서(이메일 안에 들어갈 내용)를 생성합니다.
        HtmlPart = MIMEText(self.massage_contents,'html', _charset = 'UTF-8' )
       
        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.senderAddr,"klom2683") #로그인 아이디
        s.sendmail(self.senderAddr , [self.recipientAddr], msg.as_string())
        s.close()
        
        pass


