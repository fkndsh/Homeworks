#Модуль 3. Часть 4. Задача 2.
#Добавка к функции проверки на то, есть ли такой логин в системе.

import json

def register(login, passwd):
    users_data = dict()
    while True:
        login = input("Введите логин (или Enter - выход): ")
        if login in users_data:
            print('print("Пользователь с таким именем уже существует. Введите другой логин.")')
            login = input("Введите логин (или Enter - выход): ")
        if not login:
            break
        passwd = input("Введите пароль: ")
        users_data[login]=passwd
    users_data_json=json.dumps(users_data)
    file_json=open('file.json', 'w')
    file_json.write(users_data_json)
    file_json.close()
    pass

register(login, passwd)