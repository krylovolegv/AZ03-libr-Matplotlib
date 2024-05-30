import requests
from bs4 import BeautifulSoup
import csv

# URL страницы
url = 'https://www.divan.ru/category/divany-i-kresla'

try:
    # Отправляем GET-запрос
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешный запрос
except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")
    exit(1)

# Парсим HTML-код
soup = BeautifulSoup(response.text, 'html.parser')

# Парсинг имен и цен
product_cards = soup.find_all(attrs={"data-testid": "product-card"})
print(f"Найдено {len(product_cards)} карточек продуктов.")

data = []
for card in product_cards:
    try:
        price_elem = card.find('meta', {'itemprop': 'price'})

        if price_elem is not None:
            price = price_elem.get("content").strip()
            data.append([price])
        else:
            print("Элемент не найден в карточке продукта.")

    except Exception as e:
        print(f"Ошибка при обработке карточки: {e}")

# Проверка, что данные для записи существуют
if not data:
    print("Нет данных для записи в CSV файл.")
    exit(1)

# Открытие CSV файла для записи
try:
    with open('price_divan_clear.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовки столбцов

        # Записываем данные в CSV файл
        for row in data:
            writer.writerow(row)
    print("Данные успешно записаны в CSV файл.")
except IOError as e:
    print(f"Ошибка при записи в файл: {e}")


