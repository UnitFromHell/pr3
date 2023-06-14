# import os 
# from email.mime.text import MIMEText
# import smtplib
# from random import randint    
# code = randint(100,999)

# def test(message):
#     sender = "isip_i.s.ilyin@mpt.ru"
#     password = os.getenv("crutcat2015")

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     try:
#         server.login(sender, password)
#         msg = MIMEText(message)
#         msg["Subject"] = "I see you"
#         server.sendmail(sender, sender, msg.as_string())
        
#         return "MSG sent"
#     except Exception as e:
#         return f"{e} Check login and password"

# def main():
#     message = code
#     print(test(message=message))
    
# if __name__ == "__main__":
#     main()




# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# import smtplib
# import config

# def test():
#     try:
#         tema = 'da238'
#         text = 'bruh'
#         mail = 'ilya.ilyin.200311@gmail.com'
#         fmail = 'isip_i.s.ilyin@mpt.ru'
#         password = 'wbqqmdgzxcowlhtv'

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.ehlo()

#         server.login(mail, password)

#         subject = tema
#         body = text
#         message = f'Subject: {subject}\n\n{body}'

#         server.sendmail(fmail, mail, message)
#         server.quit()

#         print('')
#         print('Yspeshno')
#     except Exception as e:
#         print(e)
#         print('Proval')
# def main():
#   test()
    
# if __name__ == "__main__":
#      main()

#xpmxqiigulxchjlv
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from random import randint    
# code = randint(100,999)


# from_email = 'isip_i.s.ilyin@mpt.ru'
# password = 'xpmxqiigulxchjlv'

# msg = MIMEMultipart()

# to_email = 'ilya.ilyin.200311@gmail.com'
# message = f'Код:{code}'

# msg.attach(MIMEText(message, 'plain'))

# server = smtplib.SMTP('smtp.gmail.com: 587')
# server.starttls()
# server.login(from_email, password)
# server.sendmail(from_email, to_email, msg.as_string())
# server.quit()








import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint    
code = randint(100,999)


from_email = 'isip_i.s.ilyin@mpt.ru'
password = 'xpmxqiigulxchjlv'

msg = MIMEMultipart()

to_email = 'ilya.ilyin.200311@gmail.com'
message = f'Код:{code}'

msg.attach(MIMEText(message, 'plain'))

while True:

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()