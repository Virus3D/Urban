import matplotlib.pyplot as plt
import numpy as np

# Генерация двух числовых списков
x = np.linspace(0, 10, 100)  # 100 чисел от 0 до 10
y1 = np.sin(x)  # Первый список синус
y2 = np.cos(x)  # Второй список косинус

# Создание линейной диаграммы
plt.figure(figsize=(10, 5))  # Размер диаграммы

# Построение первой линии (синус)
plt.plot(x, y1, label='Синус', color='blue')  
# Построение второй линии (косинус)
plt.plot(x, y2, label='Косинус', color='red')

# Настройки диаграммы
plt.title('Линейная диаграмма синуса и косинуса')  # Заголовок
plt.xlabel('Введите x')  # Подпись для оси x
plt.ylabel('Значение функции')  # Подпись для оси y
plt.legend()  # Показываем легенду
plt.grid(True)  # Включить сетку
plt.axhline(0, color='black', lw=0.5, ls='--')  # Добавление оси X
plt.axvline(0, color='black', lw=0.5, ls='--')  # Добавление оси Y

# Сохранение графика в файл
plt.savefig('module11/img/plot.png')  # Сохраняем график как PNG
plt.close()  # Закроем график, чтобы избежать предупреждений
