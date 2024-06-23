import smtplib
from email.mime.text import MIMEText

email_list = ['aaaa@gmail.com']
from_addr = 'aaaa@gmail.com'


# english email
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('aaaaa@gmail.com', '')

for i in range(0, len(email_list)):
    msg = "hello"
    to_addr = email_list[i] 
    status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
# smtp.close()
# smtp.ehlo()
smtp.quit()


# chinese email
mime = MIMEText("你好", "plain", "utf-8")
mime["Subject"] = "我很好"
mime["From"] = 'aaaa@gmail.com'
mime["To"] = 'bbbbb@ntu.edu.tw'
mime["Cc"] = "@gmail.com, @gmail.com"
msg = mime.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
# server = smtplib.SMTP()
server.connect('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(from_addr, my_pass)
status = server.sendmail(mime["From"], mime["To"], msg)
# server.close()
# server.ehlo()
server.quit()
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
