
# lesson 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for min_five in a:
#     if min_five < 5:
#         print(min_five)
# Также можно воспользоваться функцией filter, которая фильтрует элементы согласно заданному условию:
# print(list(filter(lambda min_five: min_five < 5, a)))

# И, вероятно, наиболее предпочтительный вариант решения этой задачи — списковое включение:

# print([min_five for min_five in a if min_five < 5])

# lesson 2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# resultat = []
# for elA in a:
#     if elA in b:
#         resultat.append(elA)
# print(resultat)

# Или функцией filter:
# result = list(filter(lambda elem: elem in b, a))
# Или списковым включением:
# result = [elem for elem in a if elem in b]

# lesson 3 Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
# / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

# while True:
#     a = int(input('Введите первое число '))
#     b = int(input('Введите второе число '))
#     operation = str(input('Выберите операцию, которую необходимо произвести над числами: + Сложение, - Вычитание, * Умножение, / Деление '))
#     if operation =='+':
#         print(a+b)
#         break
#     elif operation =='-':
#         print(a-b)
#         break
#     elif operation =='*':
#         print(a*b)
#         break
#     elif operation == '/':
#         print(a/b)
#         break
#     else:
#         print("Вы ошиблись с входными данными!")

# lesson 4 Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

a = int(input('Введите длину стороны квадрата '))
square = str(input('p - Найти периметр, s - Найти площадь, d - найти диагональ '))
if square =='p':
    print(4*a)
elif square == 's':
    print(2*a)
elif square == 'd':
    print((2**0.5)*a)
