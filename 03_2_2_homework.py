#Модуль 3. Часть 2. Задача 2.
#Дана рандомная матрица. Необходимо найти в ней максимальный элемент.

from random import randint
n=5
m=[[randint(0,100) for i in range(n)] for j in range (n)]
print(m)

total=sum(m,[])
print(total)
print(max(total))