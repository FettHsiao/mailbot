import smtplib

smtp = smtplib.SMTP('smtps.ntu.edu.tw', 465)
smtp.ehlo()
smtp.starttls()
smtp.login('bbbb@ntu.edu.tw', '')

from_addr = 'bbbb@ntu.edu.tw'
to_addr = 'bbbb@ntu.edu.tw'
msg = "hello"
status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()