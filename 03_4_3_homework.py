#Модуль 3. Часть 4. Задача 3.
#Функция для проверки правильности логина и пароля для входа в систему.
#Пароль должен быть не менее 3 символов. Логин должен содержать только буквы нижнего регистра.

import json

def login_function(login, passwd):
    with open ('file.json', 'r') as file:
        content=file.read()
        content_dict=json.loads(content)
    print(type(content_dict))
    for key in content_dict:
        passwd = content_dict[key]
        if key.islower()==False:
            print("Пользователь с паролем ", passwd, ". Логин должен содержать только буквы нижнего регистра." )
        if key.islower()==True:
            print("Логин указан корректно")
    for val in content_dict:
        login = content_dict[val]
        if len(val)<3:
            print(login, ", пароль должен содержать не менее 3х символов")
        else:
            print(login, ", ващ пароль указан корректно")
    pass

login_function(login, passwd)