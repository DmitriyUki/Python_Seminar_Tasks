# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# нашел это решение на просторах интернета

# eng = 'qwertyuiopasdfghjklzxcvbnm'

# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

# list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

# word = input('Введите слово на русском или английском языке: ')

# if word[0].lower() in eng:
#     summa = 0
#     for letter in word:
#         for key, value in list_English.items():
#             if letter.upper() in value:
#                 summa += key
#     print(f'стоимость введенного английского слова = {summa}')
# else:
#     if word[0].lower() in rus:
#         summa = 0
#         for letter in word:
#             for key, value in list_Russian.items():
#                 if letter.upper() in value:
#                     summa += key
#     print(f'стоимость введенного русского слова = {summa}')




def poisk_sum (price_of_word, word): # не смог разоратся, поэтому позаимствовал решение с разбора
    sum_of_price = 0
    for letter in word:
        for v_key, v_value in price_of_word.items():
            if letter.upper() in v_key:
                sum_of_price += v_value
    return sum_of_price

price_of_word = {"AEIOULNSTR" : 1, "DG" : 2, "BCMP" : 3, "FHVWY" : 4, "K" : 5,
                 "JX" : 8, "QZ" : 10, "АВЕИНОРСТ" : 1, "ДКЛМПУ" : 2, "БГЁЬЯ" : 3, "ЙЫ" : 4, "ЖЗХЦЧ" : 5, 
                 "ЭЮ" : 8,"ФЩЪ" : 10}


word = input('Введите слово для которого необходимо посчитать стоимость: ')   

print(f'Стоимость введенного слова:  {poisk_sum (price_of_word, word)}')