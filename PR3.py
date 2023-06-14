# import mysql.connector
# from mysql.connector import Error
# from config import db_config

# def connect(db_host, user_name, user_password, db_name = None):
#     connection_db = None
#     try:
#         connection_db = mysql.connector.connect(
#             host = db_host,
#             user = user_name,
#             password = user_password,
#             database = db_name
#         )
#         print("Подключились")
#     except Error as e:
#         print("Возникла ошибка", e)
#     return e

# conn = connect(db_config["mysql"]["host"],
#                db_config["mysql"]["user"],
#                db_config["mysql"]["pass"])

# cursor = conn.cursor()

# query = 'CREATE DATABASE {}'.format('Test')
# cursor.execute(query)
# cursor.close()
# conn.close()

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint    
import pymysql
from config import host, user, password, db_name
import smtplib 
from random import randint    

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

    # try:
    #     #Создание таблицы
    #     # with connection.cursor() as cursor:
    #     #     create_table_query = '''CREATE TABLE User(
    #     #     Id_User int AUTO_INCREMENT PRIMARY KEY,
    #     #     login varchar(32),
    #     #     password varchar(32)
    #     #     );'''
    #     #     cursor.execute(create_table_query)
    #     #     print("Table has been created")
    #     # #Добавление в таблицу
    #     # with connection.cursor() as cursor:
    #     #     insert_quary = '''INSERT INTO User(login, password)
    #     #     values('admin1234', 'password'),
    #     #     ('chelik', 'da238');'''
    #     #     cursor.execute(insert_quary)
    #     #     print("values added")
    #     #     connection.commit()
    # finally:
    #     connection.close()
except Exception as e:
    print("Сервис временно недоступен")
    #print(e)
# def checkRegister(plog):
#     a = '0'
#     while a != '1':
#         with connection.cursor() as cursor:
#             checkReg_quary = f'''select exists(select * from user where login = '{plog}')'''
#             checkReg2_quary = f'''select exists(select * from Employee where Login_Emp = '{plog}')'''
#             cursor.execute(checkReg_quary)
#             cursor.execute(checkReg2_quary)
#             # connection.commit()  
       
            
            
#         if(cursor.execute(checkReg2_quary)!=1 and cursor.execute(checkReg_quary) != 1):
#             a = '1'
#         else:
#             print('Такой пользователь уже есть в системе')
#         connection.commit()
print ('Команды:\n 1- Регистрация\n 2- Авторизация');
tochka = '.'
dog = '@'
check = 0
swch = int(input())
if(swch == 1):
    while(check == 0):    
        print('Введите логин(почту)')
        log = input()
        if (tochka in log and dog in log):   
                
            print('Введите пароль')
            pas = input()
            code = randint(100,999)
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
                     insert_quary = f'''INSERT INTO User(login, password)
                     values('{log}', '{pas}')'''
                     cursor.execute(insert_quary)
                     print("values added")
                     connection.commit()
                finally:
                    connection.close()
            else:
                print('Неверный код')
        else:
            print('Логин должен содержать символы @ и .')
if(swch == 2):
    print('Введите логин')
    plog = input()
    print('Введите пароль')
    ppas = input()
    with connection.cursor() as cursor:
       check_quary = f'''select exists(select * from user where login = '{plog}' and password = '{ppas}')'''
       cursor.execute(check_quary)
       
       if cursor.execute(check_quary) == 1:
            code = randint(100,999)
            from_email = 'isip_i.s.ilyin@mpt.ru'
            password = 'xpmxqiigulxchjlv'
            msg = MIMEMultipart()
            to_email = plog
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
                print('Вы авторизовались')
                
            else:
                print('Неверный код')
       else:
            print('Такого пользователя не существует. Проверьте логин и пароль')
    connection.commit()   

        