# Задача 2: Найдите сумму цифр трехзначного числа. 

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))
if 99 < number < 1000:
  a = number // 100
  b = (number % 100) // 10
  c = number % 10
  print(a + b + c)
else:
  print("Веденное число не является трехзначным")