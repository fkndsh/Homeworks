#Модуль 3. Часть 4. Задача 1.
#Функция для записи логина и пароля пользователей в файл .json

import json

def register(login, passwd):
    users_data = dict()
    while True:
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