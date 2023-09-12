import requests
from bs4 import BeautifulSoup
import json

# URL страницы, которую вы хотите спарсить
url = 'https://music.yandex.ru/artist/5054100'

# Отправляем GET-запрос на страницу
response = requests.get(url)

# Проверяем, успешно ли выполнен запрос (код 200 означает успех)
if response.status_code == 200:
    # Используем BeautifulSoup для разбора HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Создаем список для хранения данных
    data = []

    # Ищем все элементы, которые вы хотите спарсить (в данном случае, <h2> и <p>)
    headlines = soup.find_all(['h2', 'p'])

    # Итерируемся по найденным элементам и добавляем их в список данных
    for element in headlines:
        data.append(element.text)

    # Сохраняем данные в JSON файл
    with open('parsed_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print('Данные успешно спарсены и сохранены в parsed_data.json')
else:
    print('Не удалось загрузить страницу')
