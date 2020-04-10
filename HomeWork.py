# Сделать list из списка URL адресов (минимум 5).
# Написать цикл, который пробежит по списку URL и обратится
# к каждому N раз (минимум 100) с помощью библиотеки requests.
# import requests
# # print(requests.get('https://yandex.ru/').status_code)
#
# URL = [
#     'https://yandex.ru/',
#     'http://google.com/',
#     'https://www.citilink.ru/',
#     'https://www.etm.ru/',
#     'https://remontcompa.ru/'
#  ]
# # print(type(URL))
# # print(URL[1])
# for zapr in URL:
#     for _ in range(3):
#         print(requests.get(zapr).status_code)
#     print(zapr)

# print("Введите два числа")
# a = int(input("Введите число a "))
# b = int(input("Введите число b "))
# if b != 0:
#     c = a/b
#     print('a/b = ', c)
# else:
#     print("Делитель не может быть равен нулю")
#
print('Введите трехзначное число')
num = int(input('Введенное вами число '))
a = num // 100
b = num % 100 // 10
c = num % 10
sum = a + b + c
mult = a * b * c
print('Сумма чисел трехзначного число', num, 'равна', sum)
print('Произведение чисел трехзначного числа', num, 'равно', mult)
print(f'Сумма = {sum}')
print(f'Произведение = {mult}')



