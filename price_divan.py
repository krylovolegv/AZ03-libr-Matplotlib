import pandas as pd
import matplotlib.pyplot as plt

# Файл с данными
csv_file = 'price_divan_clear.csv'

try:
    # Чтение данных из CSV файла
    df = pd.read_csv(csv_file)

    # Проверка, что второй столбец существует
    if df.shape[1] < 2:
        print("CSV-файл не содержит второго столбца.")
        exit(1)

    # Извлечение цен из второго столбца
    prices = df.iloc[:, 1].dropna()  # Убираем пустые значения

    # Преобразование цен в числовой формат
    prices = pd.to_numeric(prices, errors='coerce').dropna()

    # Проверка, что данные для построения графика существуют
    if prices.empty:
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

except IOError as e:
    print(f"Ошибка при чтении файла: {e}")
    exit(1)
except pd.errors.EmptyDataError:
    print("CSV-файл пуст.")
    exit(1)
except Exception as e:
    print(f"Произошла ошибка: {e}")
    exit(1)