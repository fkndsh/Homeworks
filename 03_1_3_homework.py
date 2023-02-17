#Модуль 3. Часть 1. Задача 3.
#Посчитать сумму цифр вводимого числа.

n = list(input())
print(n)
for i,item in enumerate(n):
    n[i]=int(item)
    i=+1
for i in n:
    print(type(i))
d=0
d=sum(n)
print(d)