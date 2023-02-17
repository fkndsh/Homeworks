#Модуль 3. Часть 2. Задача 1.
#В исходном списке найти все повторяющиеся элементы и вывести их.

l=[1,4,1,6,"hello","a",5,"hello"]
l_rep=[]

for item in l:
    count = 0
    for x in l:
        if x==item:
            count+=1
            if count>=2:
                l_rep.append(x)
l_rep_set=set(l_rep)                
print(l_rep_set)