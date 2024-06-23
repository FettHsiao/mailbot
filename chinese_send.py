import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from getpass import getpass

text_list = ['你好']
email_list = ['aaaaaa@gmail.com']
from_addr = 'aaaaaaaa@gmail.com'
my_pass = getpass("input the password: ")
to_addr = 'aaaaa'

# read file
# with open("") as file:
#     file_content = file.read()

# read image

for i in range(len(text_list)):
    mime = MIMEText("請您加油", "plain", "utf-8")
# mime["Subject"] = "恭喜您中獎"
    mime["Subject"] = text_list[len(text_list)-i-1]
    mime["From"] = 'aaaa@gmail.com'
    mime["To"] = 'aaaaa@gmail.com'
    mime["Cc"] = "@gmail.com, @gmail.com"
    msg = mime.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server = smtplib.SMTP()
    server.connect('smtp.gmail.com', 587)
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.connect()
    server.ehlo()
    server.starttls()
    server.login(from_addr, my_pass)
    status = server.sendmail(from_addr, to_addr, msg)
    # server.close()
    # server.ehlo()
    server.quit()
    if status=={}:
        print("郵件傳送成功!")
    else:
        print("郵件傳送失敗!")
