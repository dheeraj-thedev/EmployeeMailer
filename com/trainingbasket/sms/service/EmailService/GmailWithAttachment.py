import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "loggerdemon@gmail.com"   #Your Email Address
toaddr = "dheeraj@trainingbasket.net"  #whom you want to send to

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL: Testing the mail"
body = "Hi all this was an automation done by me + Python core SMTP libraries"


msg.attach(MIMEText(body, 'plain'))

filename = "SimpleMailExample.png"  # NAME OF THE FILE WITH ITS EXTENSION
attachment = open("d:\\SimpleMailExample.png", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "demonlogger@1989")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
