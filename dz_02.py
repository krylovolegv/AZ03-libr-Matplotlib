import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100  # количество точек
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Создание диаграммы рассеяния
plt.scatter(x_data, y_data, color='blue', edgecolor='black')

# Кастомизация графика
plt.xlabel("X данные")
plt.ylabel("Y данные")
plt.title("Диаграмма рассеяния для случайных данных")

# Показ графика
plt.show()