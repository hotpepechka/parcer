import requests
from bs4 import BeautifulSoup

# URL страницы, которую вы хотите спарсить
url = 'https://music.yandex.ru/artist/5054100'

# Отправляем GET-запрос на страницу
response = requests.get(url)

# Проверяем, успешно ли выполнен запрос (код 200 означает успех)
if response.status_code == 200:
    # Используем BeautifulSoup для разбора HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все заголовки новостей на странице (предположим, что они находятся в тегах <h2>)
    headlines = soup.find_all('h2')

    # Выводим заголовки на экран
    for headline in headlines:
        print(headline.text)
else:
    print('Не удалось загрузить страницу')

