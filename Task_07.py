# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

i = int(input())

if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
    print("YES")
else:
    print("NO")

#     сначала надо проверить совместно кратен 4 и не кратен 100, тогда високосный
# ага, сам нарвался при первом написании
# код проще минимизировать проще работать и ощибки виднее
# Воробьев Николай 22:33
# любой год, который  делится на 400 - високосный



#Коды с семинара:
# Миронов
# i = int(input())

# if i % 4 == 0 and i % 100 != 0: 
#    print("нет")
# elif i % 400 == 0:
#     print("etv")
# Myshkovskiy Pavel 22:38
# a=int(input("Введите год "))
# if  a%4==0  and a%100!=0 :
#     print ("YES")
# elif a%400==0:
#     print("Yeeesss")
# else:
#     print("No no no")