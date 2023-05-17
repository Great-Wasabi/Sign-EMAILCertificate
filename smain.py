import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from smail import sign_message

EMAIL_ID = "XXXXXXXXXXXXXXXXXXXXXX"
EMAIL_PASSWORD = "XXXXXXXXXXXXXXXX"
SMTP_SERVER = "XXXXXXXXXXXXXXXXXXX" #For GMAIL smtp.gmail.com

CERT_FILE = "certs/certificate.pem"
PRIV_KEY = "certs/private_key.pem"

TARGET_EMAIL_ID = "YYYYYYYYYYYYYYYYY"

message = """Hello,

This is Certificate Testing using Private Key and SIgning and Python

Regards, 
PipKck"""

msg = MIMEMultipart("related")

msg.attach(MIMEText(message, 'plain', _charset='utf-8'))
msg['Subject'] = "Certificate Testing"
msg['From'] = EMAIL_ID
msg['TO'] = TARGET_EMAIL_ID

signed_msg = sign_message(msg, PRIV_KEY, CERT_FILE)

with smtplib.SMTP_SSL(SMTP_SERVER, smtplib.SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_ID, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ID, TARGET_EMAIL_ID, signed_msg.as_string())
    
print("Email Sent Successfully")