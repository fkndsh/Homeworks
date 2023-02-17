#Модуль 3. Часть 3. Задача 3.
#Есть массив. Написать функцию, которая составляет максимальное из них число.

list=[56,9,11,2]
list_vl=[]
print("Исходный список:", list)

for el in list:
    list_value=[]
    list_value.append(el)
    list_vl.append(list_value)
print("1. Создали вложенные списки: ", list_vl)

list_num_ish=[]
for el in list_vl:
    list_i=[]
    for i in el:
        i_str=str(i)
        for i in range(0, len(i_str), 1):
            list_i.append(int(i_str[i:i+1]))
        list_num_ish.append(list_i)
print("2. Разбили вложенные списки, чтобы иметь доступ к элементам: ", list_num_ish)

list_max=max(list_num_ish, key=len)
a=len(list_max)

import copy
list_num=copy.deepcopy(list_num_ish)
for el in list_num:    
    if len(el)<a:
        el.append(9)
print("3. Добавили 9, чтобы привести к одному порядку: ", list_num)

list_dop_val=[]       
for el in list_num:
    dop_val=int(''.join(map(str, el)))
    list_dop_val.append(dop_val)
print("4. Вернули обратно в список, чтобы сравнивать с исходным: ", list_dop_val)

list_dop_val_sort=sorted(list_dop_val, reverse=True)  
print("5. Отсортировали, чтобы составить максимальное число: ", list_dop_val_sort)

list_vl_dop=[]                 
for el in list_dop_val_sort:
    list_value_dop=[]
    list_value_dop.append(el)
    list_vl_dop.append(list_value_dop)
print("6. Создали вложенные списки новые: ", list_vl_dop)

list_num_dop=[]                
for el in list_vl_dop:
    list_i_dop=[]
    for i in el:
        i_str_dop=str(i)
        for i in range(0, len(i_str_dop), 1):
            list_i_dop.append(int(i_str_dop[i:i+1]))
        list_num_dop.append(list_i_dop)
print("7. Разбили отсортированный список, чтобы убрать 9: ", list_num_dop)
                 
for i in list_num_dop:
    if i in list_num_ish:
        pass
    else:
        i.remove(i[-1])
print("8. Поставили в правильном порядке числа для итога: ", list_num_dop)

list_end=[]       
for el in list_num_dop:
    dop_num_val=int(''.join(map(str, el)))
    list_end.append(dop_num_val)
print("9. Конечный список для составления числа: ", list_end)

answer = int(''.join(map(str, list_end)))
print("Ответ: ", answer)