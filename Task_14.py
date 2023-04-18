# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input("Введите степень вкоторую хотите возвести: "))
count = 0
proizv = 0
while proizv < n:
    proizv = 2 ** count
    count +=1
    if proizv < n:
        print(proizv)

