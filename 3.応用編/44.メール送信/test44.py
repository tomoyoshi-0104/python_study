import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

from_address = 'from＠xxx.xx.jp'
to_address = 'to＠xxx.xx.jp'

charset = 'ISO-2022-JP'
subject = 'メールの件名です'
text = 'メールの本文です'

msg = MIMEText(text, 'plain', charset)
msg['subject'] = Header(subject, charset)
msg['from'] = from_address
msg['to'] = to_address
msg['date'] = formatdate(localtime=True)

smtp = smtplib.SMTP('xxx.xx.jp')
smtp.sendmail(from_address, to_address, msg.as_string())
smtp.close()
