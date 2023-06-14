from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint    
import pymysql
from config import host, user, password, db_name
import smtplib 
import datetime

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

def history_view_emp(eml):
    
    with connection.cursor() as cursor:
        quary = f"select * from user where login = '{eml}'"
        cursor.execute(quary)
        for user in cursor.fetchall():
            id = int(f"{user['ID_User']}")
        quary2 = f"select chek from chek where User_ID = '{id}'"
        cursor.execute(quary2)
        results = list(cursor.fetchall())
        print (results)
    
def history_view():
    global logi
    with connection.cursor() as cursor:
        quary = f'''select * from user where login = '{logi}' '''
        cursor.execute(quary)
        for user in cursor.fetchall():
            id = int(f"{user['ID_User']}")
        quary2 = f"select chek from chek where User_ID = '{id}'"
        cursor.execute(quary2)
        results = list(cursor.fetchall())
        print (results)
        
        
def zakaz():
    global bln
    global logi
    global pass0rd
    tomatos_in_zakaz = 0
    eggs_in_zakaz = 1
    onion_in_zakaz = 0
    carrot_in_zakaz = 1
    beef_in_zakaz = 2
    potatos_in_zakaz = 0
    peggs_in_zakaz = 0
    chicken_in_zakaz = 0
    pasta_in_zakaz = 1
    sous_in_zakaz = 1
    with connection.cursor() as cursor:
        tarakan = randint(0,5)
        quary = '''select * from bludo '''
        cursor.execute(quary)
        for bludo in cursor.fetchall():
            bludo_cost = int(f"{bludo['cost']}")
        quaryPr = '''select * from cklad '''
        cursor.execute(quaryPr)
        for cklad in cursor.fetchall():
            Tomatos = int(f"{cklad['Tomatos']}")
            Eggs = int(f"{cklad['Eggs']}")
            Onion = int(f"{cklad['Onion']}")
            Carrot = int(f"{cklad['Carrot']}")
            Beef = int(f"{cklad['Beef']}")
            Potatos = int(f"{cklad['Potatos']}")
            Peggs = int(f"{cklad['Peggs']}")
            Chicken = int(f"{cklad['Сhicken']}")
            Pasta = int(f"{cklad['Pasta']}")
            Sous = int(f"{cklad['Sous']}")
        global bal
        global card
        v = int(input('Стандартный рамен включает в себя: 1 яйцо, 1 морковь, 2 куска говядины, 1 порцию лапши и 1 порцию соевого соуса\n 1- Продолжить; 2 - изменить\n'))
       
        if(v == 1):
            kolvo = int(input('Сколько вы хотите блюд?\n'))
            eggs_in_zakaz *= kolvo
            tomatos_in_zakaz *= kolvo
            onion_in_zakaz *= kolvo
            carrot_in_zakaz *= kolvo
            beef_in_zakaz *= kolvo
            potatos_in_zakaz *= kolvo
            peggs_in_zakaz *= kolvo
            chicken_in_zakaz *= kolvo
            pasta_in_zakaz *= kolvo
            sous_in_zakaz *= kolvo
            if(Tomatos - tomatos_in_zakaz >= 0 and Eggs - eggs_in_zakaz >= 0 and Onion - onion_in_zakaz >= 0 and Carrot - carrot_in_zakaz >= 0 and Beef- beef_in_zakaz >= 0 and Potatos - potatos_in_zakaz >= 0 and Peggs - peggs_in_zakaz >= 0 and Chicken - chicken_in_zakaz >= 0 and Pasta - pasta_in_zakaz >= 0 and Sous - sous_in_zakaz >= 0):
                x = kolvo // 5
                if(bal - bludo_cost * (kolvo-x) >= 0 ):
                    if(tarakan == 5):
                        print('Простите! В заказ попал таракан, мы сделаем вам скидку 30%')
                        if(card == 'бронзовая'):
                            bal = (bal - bludo_cost * (kolvo - x) * 0.7 * 0.95)
                            bal = bal + bal
                        if(card == 'серебряная'):
                            bal = (bal - bludo_cost * (kolvo - x) * 0.7 * 0.9)
                            bal = bal + bal
                        if(card == 'золотая'):
                            bal = (bal - bludo_cost * (kolvo - x) * 0.7 * 0.8)
                            bal = bal + bal
                        else:
                            bal = bal - bludo_cost * (kolvo - x) * 0.7
                            bal = bal + bal
                    
                    
                    
                        quaryT = f"UPDATE user set balance = '{bal}' where login = '{logi}'"
                        cursor.execute(quaryT)
                        quaryCard = f"select * from user where login = '{logi}'"
                        cursor.execute(quaryCard)
                        
                        for user in cursor.fetchall():
                            card = f"{user['card']}"
                            idishnik = f"{user['ID_User']}"
                            loginchik = f"{user['login']}"
                        if(bludo_cost * (kolvo - x) * 0.7 >= 5000 and bludo_cost * (kolvo - x) * 0.7 <15000 and card != 'серебряная' and card != 'золотая'):
                            quaryC = f"UPDATE user set card = 'бронзовая' where login = '{logi}'"
                            cursor.execute(quaryC)
                        elif(bludo_cost * (kolvo - x) * 0.7 >= 15000 and bludo_cost * (kolvo - x) * 0.7 < 25000 and card != 'золотая'):
                            quaryC = f"UPDATE user set card = 'серебряная' where login = '{logi}'"
                            cursor.execute(quaryC)
                        elif( bludo_cost * (kolvo - x) * 0.7 >= 25000 ):
                            quaryC = f"UPDATE user set card = 'золотая' where login = '{logi}'"
                            cursor.execute(quaryC)
                        now = datetime.datetime.now()
                        formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
                        chek_number = randint(1000000000, 9999999999)
                        tbl = randint(1,9)
                        quaryChek = f"INSERT INTO history(history, User_ID) values('Чек№:{chek_number}; Ресторан: TarakanShop; Стлол№ {tbl}; Блюдо: Рамен классический({kolvo}шт.), Таракан(30%); Сумма: {bludo_cost * (kolvo - x)}руб. дата: {formatted_time}', '{idishnik}')"
                        cursor.execute(quaryChek)
                        quaryData = f"INSERT INTO chek(chek, User_ID) values('Кол-во раменов: {kolvo} Дата: {formatted_time}', '{idishnik}')"
                        check_msg = f"Чек№:{chek_number};\n Ресторан: TarakanShop;\n Стлол№ {tbl};\n Блюдо: Рамен классический({kolvo}шт.)\n Таракан(30%);\n Сумма: {bludo_cost * (kolvo - x)}руб.\n Дата: {formatted_time}\n"
                        cursor.execute(quaryData)
                        connection.commit()
                       
                        from_email = 'isip_i.s.ilyin@mpt.ru'
                        password = 'xpmxqiigulxchjlv'
                        msg = MIMEMultipart()
                        to_email = logi
                        message = check_msg
                        msg.attach(MIMEText(message, 'plain'))
                        msg['Subject'] = 'Чек'
                        server = smtplib.SMTP('smtp.gmail.com: 587')
                        server.starttls()
                        server.login(from_email, password)
                        server.sendmail(from_email, to_email, msg.as_string())
                        server.quit()
                        print('Спасибо за заказ')
                        quaryProduct = f"Update cklad set Tomatos = {Tomatos - tomatos_in_zakaz} where ID_cklad = 1"
                        quaryProduct2 = f"Update cklad set Eggs = {Eggs - eggs_in_zakaz} where ID_cklad = 1"
                        quaryProduct3 = f"Update cklad set Onion = {Onion - onion_in_zakaz} where ID_cklad = 1"
                        quaryProduct4 = f"Update cklad set Carrot = {Carrot - carrot_in_zakaz} where ID_cklad = 1"
                        quaryProduct5 = f"Update cklad set Beef = {Beef - beef_in_zakaz} where ID_cklad = 1"
                        quaryProduct6 = f"Update cklad set Potatos = {Potatos - potatos_in_zakaz} where ID_cklad = 1"
                        quaryProduct7 = f"Update cklad set Peggs = {Peggs - peggs_in_zakaz} where ID_cklad = 1"
                        quaryProduct8 = f"Update cklad set Сhicken = {Chicken - chicken_in_zakaz} where ID_cklad = 1"
                        quaryProduct9 = f"Update cklad set Pasta = {Pasta - pasta_in_zakaz} where ID_cklad = 1"
                        quaryProduct10 = f"Update cklad set Sous = {Sous - sous_in_zakaz} where ID_cklad = 1"
                        cursor.execute(quaryProduct)
                        cursor.execute(quaryProduct2)
                        cursor.execute(quaryProduct3)
                        cursor.execute(quaryProduct4)
                        cursor.execute(quaryProduct5)
                        cursor.execute(quaryProduct6)
                        cursor.execute(quaryProduct7)
                        cursor.execute(quaryProduct8)
                        cursor.execute(quaryProduct9)
                        cursor.execute(quaryProduct10)     
                    elif(tarakan >= 0 and tarakan < 5):
                        if(card == 'бронзовая'):
                            bal = bal - bludo_cost * (kolvo - x)  * 0.95
                            bal = bal + bal
                        if(card == 'серебряная'):
                            bal = bal - bludo_cost * (kolvo - x)  * 0.9
                            bal = bal + bal
                        if(card == 'золотая'):
                            bal = bal - bludo_cost * (kolvo - x)  * 0.8
                            bal = bal + bal
                        else:
                            bal = bal - bludo_cost * (kolvo - x)
                            bal = bal + bal
                        quaryT = f"UPDATE user set balance = '{bal}' where login = '{logi}'"
                        cursor.execute(quaryT)
                        quaryCard = f"select * from user where login = '{logi}'"
                        cursor.execute(quaryCard)
                        for user in cursor.fetchall():
                            card = f"{user['card']}"
                            idishnik = f"{user['ID_User']}"
                        if(bludo_cost * (kolvo - x)  >= 5000 and bludo_cost * (kolvo - x)  <15000 and bludo_cost * (kolvo - x)  != 'серебряная' and card != 'золотая'):
                            quaryC = f"UPDATE user set card = 'бронзовая' where login = '{logi}'"
                            cursor.execute(quaryC)
                        elif(bludo_cost * (kolvo - x)  >= 15000 and bludo_cost * kolvo  < 25000 and bludo_cost * (kolvo - x)  != 'золотая'):
                            quaryC = f"UPDATE user set card = 'серебряная' where login = '{logi}'"
                            cursor.execute(quaryC)
                        elif( bludo_cost * (kolvo - x)  >= 25000 ):
                            quaryC = f"UPDATE user set card = 'золотая' where login = '{logi}'"
                            cursor.execute(quaryC)
                        
                        now = datetime.datetime.now()
                        formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
                        chek_number = randint(1000000000, 9999999999)
                        tbl = randint(1,9)
                        quaryChek = f"INSERT INTO history(history, User_ID) values('Чек:{chek_number}; Ресторан: TarakanShop; Стлол№ {tbl}; Блюдо: Рамен классический; Кол-во {kolvo}; Сумма: {bludo_cost * (kolvo - x)}руб. дата: {formatted_time}', '{idishnik}')"
                        check_msg = f"Чек№ {chek_number};\nРесторан: TarakanShop;\n Стлол№ {tbl};\n Блюдо: Рамен классический;\n Кол-во {kolvo}шт.;\n Сумма: {bludo_cost * (kolvo - x)}руб.\n Дата: {formatted_time}\n"
                        cursor.execute(quaryChek)
                        
                        from_email = 'isip_i.s.ilyin@mpt.ru'
                        password = 'xpmxqiigulxchjlv'
                        msg = MIMEMultipart()
                        to_email = logi
                        message = check_msg
                        msg.attach(MIMEText(message, 'plain'))
                        msg['Subject'] = 'Чек'
                        server = smtplib.SMTP('smtp.gmail.com: 587')
                        server.starttls()
                        server.login(from_email, password)
                        server.sendmail(from_email, to_email, msg.as_string())
                        server.quit()
                        quaryData = f"INSERT INTO chek(chek, User_ID) values('Кол-во раменов: {kolvo} Дата: {formatted_time}', '{idishnik}')"
                        cursor.execute(quaryData)
                        connection.commit()
                        print('Чек отправлен вам на почту')
                        print('Спасибо за заказ!')
                        quaryProduct = f"Update cklad set Tomatos = {Tomatos - tomatos_in_zakaz} where ID_cklad = 1"
                        quaryProduct2 = f"Update cklad set Eggs = {Eggs - eggs_in_zakaz} where ID_cklad = 1"
                        quaryProduct3 = f"Update cklad set Onion = {Onion - onion_in_zakaz} where ID_cklad = 1"
                        quaryProduct4 = f"Update cklad set Carrot = {Carrot - carrot_in_zakaz} where ID_cklad = 1"
                        quaryProduct5 = f"Update cklad set Beef = {Beef - beef_in_zakaz} where ID_cklad = 1"
                        quaryProduct6 = f"Update cklad set Potatos = {Potatos - potatos_in_zakaz} where ID_cklad = 1"
                        quaryProduct7 = f"Update cklad set Peggs = {Peggs - peggs_in_zakaz} where ID_cklad = 1"
                        quaryProduct8 = f"Update cklad set Сhicken = {Chicken - chicken_in_zakaz} where ID_cklad = 1"
                        quaryProduct9 = f"Update cklad set Pasta = {Pasta - pasta_in_zakaz} where ID_cklad = 1"
                        quaryProduct10 = f"Update cklad set Sous = {Sous - sous_in_zakaz} where ID_cklad = 1"
                        cursor.execute(quaryProduct)
                        cursor.execute(quaryProduct2)
                        cursor.execute(quaryProduct3)
                        cursor.execute(quaryProduct4)
                        cursor.execute(quaryProduct5)
                        cursor.execute(quaryProduct6)
                        cursor.execute(quaryProduct7)
                        cursor.execute(quaryProduct8)
                        cursor.execute(quaryProduct9)
                        cursor.execute(quaryProduct10)     
                else:
                    print('Недостаточно средств')
            ##if (v == 2):
            else:
                print('Недостаточно ингридиентов')   ##  v2 = int(input("1 - Добавить"))
        else:
            print('Неизвестная команда')    
        
                
        connection.commit()
      ##  b = {}
        ##b = {'1': 'Лапша 1 порция', '2':'2 Куска говядины', '3': '1 порция соевого соуса', '4': '1 яйцо', '5': '1 морковь'}
        ##print('Рамен состоит из:')
        ##for key in b:
         ##   print(b[key])
        ##z = int(input("1 - Продолжить; 2 - Изменить блюдо" ))
        
            
   
def reg(log, pas):
    tochka = '.'
    dog = '@'
    check = 0
    if (tochka in log and dog in log):
        with connection.cursor() as cursor:
            check_quary = f'''select * from user where login = %s''' 
            q = f'''select * from bludo where Id_bludo = 1'''
            cursor.execute(q)
            for bludo in cursor.fetchall():
                global cost_bludo
                cost_bludo = int(f"{bludo['cost']}")
            val = (log)
            cursor.execute(check_quary, val)
            result = cursor.fetchall()
            rnd = randint(1200, 1400)
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
                            values('{log}', '{pas}','','{rnd}')'''
                            cursor.execute(insert_quary)
                            connection.commit()
                    finally:
                        connection.close()
                    main()
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
    global bal
    global card
    bal = 0
    with connection.cursor() as cursor:
     

       check_quary = f'''select * from user where login = %s and password = %s''' 
       val = (log, pas)
       cursor.execute(check_quary, val)
     
       
       for user in cursor.fetchall(): 
            bal = int(f"{user['balance']}")
            card = f"{user['card']}"
       
       
    ##with connection.cursor() as cursor2:
       ##  check_quary2 = f'''select balance from user where login = %s and password = %s''' 
     ##    val = (log, pas)
     ##    cursor2.execute(check_quary2, val)
    ##     result2 = cursor2.fetchall()
         
  ##  if result2 != ():
   ##     bal = result2[0]
   ##     print (bal)
   ##     bal = bal + bal
        
    result = cursor.fetchall()    
    if result != ():
        
        code = randint(1000,9999)
        from_email = 'isip_i.s.ilyin@mpt.ru'
        password = 'xpmxqiigulxchjlv'
        msg = MIMEMultipart()
        to_email = log
        message = f'Ваш код: {code}'
        msg.attach(MIMEText(message, 'plain'))
        msg['Subject'] = 'Код подтверждения'
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
id = 0
balance_emp = 0
def auth2(log, pas):
        check2=0
        with connection.cursor() as cursor:
       
            check_quary = f'''select * from employee where Login_Emp = %s and Password_Emp = %s''' 
            val = (log, pas)
            cursor.execute(check_quary, val)
            result = cursor.fetchall()
       

            if result != ():
                    code = randint(1000,9999)
                    from_email = 'isip_i.s.ilyin@mpt.ru'
                    password = 'xpmxqiigulxchjlv'
                    msg = MIMEMultipart()
                    to_email = log
                    message = f'Ваш код: {code}'
                    msg.attach(MIMEText(message, 'plain'))
                    msg['Subject'] = 'Код подтверждения'
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
                        
                        with connection.cursor() as cursor:
                            quary = f'''select * from employee where Login_Emp = %s'''
                            val = (log)
                            cursor.execute(quary, log)
                            for emploee in cursor.fetchall():
                                global id 
                                global balance_emp
                                id = f"{emploee['ID_Emp']}"
                                balance_emp = f"{emploee['balance']}"
                           
                    else:
                        print('Неверный код')
                        vod2()
            else:
                print('Такого сотрудника не существует. Проверьте логин и пароль')
                vod2()
def zakup():
    
    tomatos = 0
    eggs = 0
    onion = 0
    carrot = 0
    beef = 0
    potatos = 0
    peggs = 0
    chicken = 0
    pasta = 0
    sous = 0
    ptomatos = int(50)
    preggs = 60
    ponion = 70
    pcarrot = 80
    pbeef = 90
    ppotatos  = 100
    ppreggs  = 110
    pchicken  = 120
    ppasta  = 130
    psous  = 140
    with connection.cursor() as cursor:
        quary = '''select * from cklad '''
        cursor.execute(quary)
        for cklad in cursor.fetchall():
            tomatos = int(f"{cklad['Tomatos']}")
            eggs = int(f"{cklad['Eggs']}")
            onion = int(f"{cklad['Onion']}")
            carrot = int(f"{cklad['Carrot']}")
            beef = int(f"{cklad['Beef']}")
            potatos = int(f"{cklad['Potatos']}")
            peggs = int(f"{cklad['Peggs']}")
            chicken = int(f"{cklad['Сhicken']}")
            pasta = int(f"{cklad['Pasta']}")
            sous = int(f"{cklad['Sous']}")
        can2 = 0
        while can2 != 11:  
            print('Что закупаем?: \n 1- Томаты\n 2- Яйца\n 3- Лук\n 4- Морковь\n 5- Говядина\n 6- Картошка\n 7- Перепелиные яйца\n 8- Курица\n 9- Лапша\n 10- Соевый соус\n 11 - ничего')
            can2 = int(input())
            global balance_emp
            if can2 == 1:
               ## print(tomatos)
                
                print('Введите кол-во томатов')
                tom = int(input())
               
               ## print (balance_emp)
                if int(balance_emp) - int(tom) * int(ptomatos) >= 0:
                    tomatos = int(tomatos) + int(tom)
                    balance_emp = int(balance_emp) - int(tom) * int(ptomatos)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Tomatos = {tomatos} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 2:
               ## print(tomatos)
                
                print('Введите кол-во яиц')
                eg = int(input())
              
               ## print (balance_emp)
                if int(balance_emp) - int(eg) * int(preggs) >= 0:
                    eggs = int(eggs) + int(eg)
                    balance_emp = int(balance_emp) - int(eg) * int(preggs)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Eggs = {eggs} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 3:
               ## print(tomatos)
                
                print('Введите кол-во лука')
                on = int(input())
               
               ## print (balance_emp)
                if int(balance_emp) - int(on) * int(ponion) >= 0:
                    onion = int(onion) + int(on)
                    balance_emp = int(balance_emp) - int(on) * int(ponion)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Onion = {onion} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 4:
               ## print(tomatos)
                
                print('Введите кол-во моркови')
                car = int(input())
              
               ## print (balance_emp)
                if int(balance_emp) - int(car) * int(pcarrot) >= 0:
                    carrot = int(carrot) + int(car)
                    balance_emp = int(balance_emp) - int(car) * int(pcarrot)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Carrot = {carrot} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 5:
               ## print(tomatos)
                
                print('Введите кол-во говядины')
                be = int(input())
             
               ## print (balance_emp)
                if int(balance_emp) - int(be) * int(pbeef) >= 0:
                    beef = int(beef) + int(be)
                    balance_emp = int(balance_emp) - int(be) * int(pbeef)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Beef = {beef} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 6:
               ## print(tomatos)
                
                print('Введите кол-во Картошки')
                po = int(input())
              
               ## print (balance_emp)
                if int(balance_emp) - int(po) * int(ppotatos) >= 0:
                    potatos = int(potatos) + int(po)
                    balance_emp = int(balance_emp) - int(po) * int(ppotatos)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Potatos = {potatos} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 7:
               ## print(tomatos)
                
                print('Введите кол-во перепелиных яиц')
                peg = int(input())
              
               ## print (balance_emp)
                if int(balance_emp) - int(peg) * int(ppreggs) >= 0:
                    peggs = int(peggs) + int(peg)
                    balance_emp = int(balance_emp) - int(peg) * int(ppreggs)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Peggs = {peggs} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 8:
               ## print(tomatos)
                
                print('Введите кол-во курицы')
                сhik = int(input())
              
               ## print (balance_emp)
                if int(balance_emp) - int(сhik) * int(pchicken) >= 0:
                    chicken = int(chicken) + int(сhik)
                    balance_emp = int(balance_emp) - int(сhik) * int(pchicken)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Сhicken = {chicken} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 9:
               ## print(tomatos)
                
                print('Введите кол-во лапши')
                pas = int(input())
              
               ## print (balance_emp)
                if int(balance_emp) - int(pas) * int(ppasta) >= 0:
                    pasta = int(pasta) + int(pas)
                    balance_emp = int(balance_emp) - int(pas) * int(ppasta)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Pasta = {pasta} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            if can2 == 10:
               ## print(tomatos)
                
                print('Введите кол-во сойвового соуса')
                so = int(input())
               
               ## print (balance_emp)
                if int(balance_emp) - int(so) * int(psous) >= 0:
                    sous = int(sous) + int(so)
                    balance_emp = int(balance_emp) - int(so) * int(psous)
                    quaryB = f"UPDATE employee set balance = {balance_emp} where ID_Emp = {id}"
                    cursor.execute(quaryB)
                    quary_t = f"update cklad set Sous = {sous} where ID_cklad = 1"
                    cursor.execute(quary_t)
                    ##print(tomatos)
                  ##  print (balance_emp)
                    connection.commit()
                else: 
                    print('Недостаточно средств')
            
                
    
def main():    
    global logi
    global pass0rd
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
        vbor = int(input("Чего желаете?: 1 - Сделать заказ; 2 - посмотреть историю заказов\n"))
        if (vbor == 1):
           zakaz()
        if (vbor == 2):
            history_view()
       

            
        
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
        print('Заработаем еще больше денег')
        print('Что делаем?:\n 1- Закупаем \n 2- Смотрим историю')
        can = int(input())
        if can == 1:
            zakup()
        if can == 2:
            eml = input('Введите логин клиента\n')
            history_view_emp(eml)
       
            
    elif(swch != 1 and swch != 2 and swch!=3 and swch!=4):
        print('Неизвестная команда')
print ('Команды:\n 1- Регистрация(пользователь)\n 2- Авторизация(пользователь)\n 3- Регистрация(сотрудник)\n 4- Авторизация (сотрудник)');
swch = input()
try:
    swch = int(swch)
except:
    print('Недопустим ввод букв')
main()