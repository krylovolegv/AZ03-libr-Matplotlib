import csv
import matplotlib.pyplot as plt

# Файл с данными
csv_file = 'price_divan_clear.csv'

# Чтение данных из CSV файла
prices = []

try:
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            if len(row) > 0 and row[0]:  # Проверяем, что в строке есть хотя бы один элемент и он не пустой
                try:
                    price = float(row[0])
                    prices.append(price)
                except ValueError:
                    print(f"Некорректное значение цены: {row[0]}")
except IOError as e:
    print(f"Ошибка при чтении файла: {e}")
    exit(1)

# Проверка, что данные для построения графика существуют
if not prices:
    print("Нет данных для построения гистограммы.")
    exit(1)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=30, edgecolor='black')  # bins - количество столбцов в гистограмме
plt.title('Гистограмма цен диванов')
plt.xlabel('Цена')
plt.ylabel('Количество')
plt.grid(True)

# Сохранение гистограммы как изображения (необязательно)
plt.savefig('price_histogram.png')

# Отображение гистограммы
plt.show()