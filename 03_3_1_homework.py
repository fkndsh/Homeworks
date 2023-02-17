#Модуль 3. Часть 3. Задача 1.
#Написать функцию для расчета площади треугольника по трем сторонам.

a = int(input())
b = int(input())
c = int(input())

def square(a, b, c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**(0.5)
    return s

result = square(a,b,c)
print(result)