__author__ = 'Вторушин Марк Викторович'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# РЕШЕНИЕ ЗАДАЧИ №1

# Дан список фруктов.
fruits = {'1': 'яблоко', '2': 'банан', '3': 'киви', '4': 'арбуз'} #Используем словарь для хранения ключей и значений
for key, value in fruits.items(): # С помощью цикла пробегаем по словарю
    print(key, '{:>10}'.format(value)) # и делаем вывод оставляя ключи на исходном месте,
                                       # а значения выравнивая по правой стороне


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# РЕШЕНИЕ ЗАДАЧИ №2
# Импортируем модуль random
import random
print("Решение задачи №2")
# Создаем пустые массивы
a = []
b = []
# Используем цикл для заполнения массива a
for i in range(7):
    numbers = round(random.random() * 100)  # Берем целые числа в диапазоне от 0 до 100
    a.append(numbers)
print("Исходный мыссив чисел A =", a)

i = 0
# Прогоняем цикл с условием в заданном диапазоне чисел
while i < len(a):
    if 25 < a[i] < 75:
        b.append(a[i])
        del a[i]        # Отбрасываем совпадающие числа
    else:
            i += 1
# Выводим результат
print("Массив B =", b)
print("Массив А после удаления чисел =", a)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# РЕШЕНИЕ ЗАДАЧИ №3
# Импортируем модуль random
import random
print("Решение задачи №3")
# Создаем пустые массивы
a = []
b = []
# Используем цикл для заполнения массива a целыми числами

for i in range(10):
    numbers = round(random.random() * 100)  # Берем целые числа в диапазоне от 0 до 100
    a.append(numbers)

for i in a:
    if (i % 2) == 0:
        x = i / 4
        b.append(x)
    else:
        x = i * 2
        b.append(x)


print("Исходный массив A =", a)
print("B =", b)