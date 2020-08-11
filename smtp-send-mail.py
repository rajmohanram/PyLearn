import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()

# login with application password
server.login('ram.rajmohanr@gmail.com', 'mdmdmdmdm')

msg = MIMEMultipart()
msg['From'] = "Rajmohan R"
msg['To'] = "sugdev11t@gmail.com"
msg['Subject'] = "A Test Email"

# email body
message = "This is a test mail sent from Python Application."
msg.attach(MIMEText(message, 'plain'))

# attachment
filename = 'mypic.jpeg'
attachment = open(filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

# send email
text = msg.as_string()
server.sendmail('ram.rajmohanr@gmail.com', 'sugdev11t@gmail.com', text)