import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "botgenericogratis@gmail.com"
my_password = r"B0tg3n3r1c0"

you = "jeanpablosousarabelo@gmail.com"
time = str(datetime.datetime.now())

msg = MIMEMultipart('alternative')
msg['Subject'] = "Teste Subject. Hora: " + time
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Teste no HTML Body</p></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

s.sendmail(me, you, msg.as_string())

print(s)

s.quit()

print('O programa rodou')
