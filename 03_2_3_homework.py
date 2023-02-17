#Модуль 3. Часть 2. Задача 3.
#Дан словарь. Нужно поменять местами ключи и значения.

d = {
    'name1':'id1', 
    'name2':'id2',
    'name3':'id3'
    }
d_rev=dict(reversed(item) for item in d.items())
print(d_rev)