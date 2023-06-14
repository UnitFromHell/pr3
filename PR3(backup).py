from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint    
import pymysql
from config import host, user, password, db_name
import smtplib 


try:
    connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=db_name,
    port=3306,
    # bind_address="127.0.0.1"
    cursorclass=pymysql.cursors.DictCursor
    )
   # print("Connected")
    print("#" * 20)
except Exception as e:
    print("Сервис временно недоступен")

    

def zakaz():
    
    print('Рамен: ')
def reg(log, pas):
    tochka = '.'
    dog = '@'
    check = 0
    if (tochka in log and dog in log):
        with connection.cursor() as cursor:
            check_quary = f'''select * from user where login = %s''' 
            val = (log)
            cursor.execute(check_quary, val)
            result = cursor.fetchall()
            if result == ():
                code = randint(1000,9999)
                from_email = 'isip_i.s.ilyin@mpt.ru'
                password = 'xpmxqiigulxchjlv'
                msg = MIMEMultipart()
                to_email = log
                message = f'Ваш код: {code}'
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())
                server.quit()
                print('Введите код подтверждения')
                codeA = int(input())
                if code == codeA:
                    check = 1
                    print('Спасибо за регистрацию')
                    try:
                        with connection.cursor() as cursor:
                            insert_quary = f'''INSERT INTO User(login, password, card, balance)
                            values('{log}', '{pas}','','{code}')'''
                            cursor.execute(insert_quary)
                            connection.commit()
                    finally:
                        connection.close()
                else:
                    print('Неверный код')
            else:
             print('Пользователь с таким логином уже есть в системе')
    else:
        print('Логин должен содержать символы @ и .')
def vod():
    print('Введите логин(почту)')
    logi = input()
    print('Введите пароль')
    pass0rd = input()
    auth(logi, pass0rd)
def auth(log, pas):
    check2=0
    
    with connection.cursor() as cursor:
      #  f'''select exists(select count(1) from user where login = '{log}' && password = '{pas}')'''
      # check_quary = '''(select * from user where login = '{log}' && password = '{pas}')'''
       check_quary = f'''select * from user where login = %s and password = %s''' 
       val = (log, pas)
       cursor.execute(check_quary, val)
       result = cursor.fetchall()
       
       #aleksandrsamyj64@gmail.com
       #cursor.execute(check_quary)
      
    if result != ():
        code = randint(1000,9999)
        from_email = 'isip_i.s.ilyin@mpt.ru'
        password = 'xpmxqiigulxchjlv'
        msg = MIMEMultipart()
        to_email = log
        message = f'Ваш код: {code}'
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print('Введите код подтверждения')
        codeA = int(input())
        if code == codeA:
            check2 = 1
            print('Вы авторизовались')
                    
        else:
            print('Неверный код')
            vod()
    else:
        print('Такого пользователя не существует. Проверьте логин и пароль')
        vod()

def reg2(log, pas):
    tochka = '.'
    dog = '@'
    check = 0
    if (tochka in log and dog in log):
        with connection.cursor() as cursor:
            check_quary = f'''select * from employee where Login_Emp = %s''' 
            val = (log)
            cursor.execute(check_quary, val)
            result = cursor.fetchall()
            if result == ():
                code = randint(1000,9999)
                from_email = 'isip_i.s.ilyin@mpt.ru'
                password = 'xpmxqiigulxchjlv'
                msg = MIMEMultipart()
                to_email = log
                message = f'Ваш код: {code}'
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())
                server.quit()
                print('Введите код подтверждения')
                codeA = int(input())
                if code == codeA:
                    check = 1
                    print('Спасибо за регистрацию')
                    try:
                        with connection.cursor() as cursor:
                            insert_quary = f'''INSERT INTO Employee(Login_Emp, Password_Emp, balance)
                            values('{log}', '{pas}', {code})'''
                            cursor.execute(insert_quary)
                            connection.commit()
                    finally:
                        connection.close()
                else:
                    print('Неверный код')
            else:
                print('Сотрудник с таким логином уже существует')
    else:
        print('Логин должен содержать символы @ и .')
def vod2():
    print('Введите логин(почту)')
    logi = input()
    print('Введите пароль')
    pass0rd = input()
    auth2(logi, pass0rd)
def auth2(log, pas):
        check2=0
        with connection.cursor() as cursor:
        #  f'''select exists(select count(1) from user where login = '{log}' && password = '{pas}')'''
        # check_quary = '''(select * from user where login = '{log}' && password = '{pas}')'''
            check_quary = f'''select * from employee where Login_Emp = %s and Password_Emp = %s''' 
            val = (log, pas)
            cursor.execute(check_quary, val)
            result = cursor.fetchall()
       
       #aleksandrsamyj64@gmail.com
       #cursor.execute(check_quary)
            if result != ():
                    code = randint(1000,9999)
                    from_email = 'isip_i.s.ilyin@mpt.ru'
                    password = 'xpmxqiigulxchjlv'
                    msg = MIMEMultipart()
                    to_email = log
                    message = f'Ваш код: {code}'
                    msg.attach(MIMEText(message, 'plain'))
                    server = smtplib.SMTP('smtp.gmail.com: 587')
                    server.starttls()
                    server.login(from_email, password)
                    server.sendmail(from_email, to_email, msg.as_string())
                    server.quit()
                    print('Введите код подтверждения')
                    codeA = int(input())
                    if code == codeA:
                        check2 = 1
                        print('Вы авторизовались')
                        
                    else:
                        print('Неверный код')
                        vod2()
            else:
                print('Такого сотрудника не существует. Проверьте логин и пароль')
                vod2()

def main():    
           
    if(swch == 1):
        print('Введите логин(почту)')
        logi = input()
        print('Введите пароль')
        pass0rd = input()
        reg(logi, pass0rd)
    elif(swch == 2):
        print('Введите логин')
        logi = input()
        print('Введите пароль')
        pass0rd = input()
        auth(logi, pass0rd)
        print('test')
    if(swch == 3):
        print('Введите логин(почту)')
        logi = input()
        print('Введите пароль')
        pass0rd = input()
        reg2(logi, pass0rd)
    elif(swch == 4):
        print('Введите логин')
        logi = input()
        print('Введите пароль')
        pass0rd = input()
        auth2(logi, pass0rd)
        print('test2')
    elif(swch != 1 and swch != 2 and swch!=3 and swch!=4):
        print('Неизвестная команда')
print ('Команды:\n 1- Регистрация(пользователь)\n 2- Авторизация(пользователь)\n 3- Регистрация(сотрудник)\n 4- Авторизация (сотрудник)');
swch = input()
try:
    swch = int(swch)
except:
    print('Недопустим ввод букв')
main()