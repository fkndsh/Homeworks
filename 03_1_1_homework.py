#Модуль 3. Часть 1. Задача 1.
#Определить, через сколько лет вклад будет составлять не менее указанной суммы.

x = int(input())
p = float(input())
y = int(input())

l = []
while x < y:
    x = x + x*p/100
    x = int(x)
    l.append(x)
print(l)
print ('Ответ: Через ', len(l), 'лет')