import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GmailMailer():
    def sendMail(self,emailAddress,subject, body):
        fromaddr = "loggerdemon@gmail.com"  # Your Email Address
        toaddr = emailAddress  # whom you want to send to
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        #body = "Hi all this was an automation done by me + Python with core SMTP libraries"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "demonlogger@1989")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("an email with subject was sent successfully ")
