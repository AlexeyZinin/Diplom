# Сделать list из списка URL адресов (минимум 5).
# Написать цикл, который пробежит по списку URL и обратится
# к каждому N раз (минимум 100) с помощью библиотеки requests.
import requests
# print(requests.get('https://yandex.ru/').status_code)

URL = [
    'https://yandex.ru/',
    'http://google.com/',
    'https://www.citilink.ru/',
    'https://www.etm.ru/',
    'https://remontcompa.ru/'
 ]
# print(type(URL))
# print(URL[1])
for zapr in URL:
    for _ in range(3):
        print(requests.get(zapr).status_code)
    print(zapr)