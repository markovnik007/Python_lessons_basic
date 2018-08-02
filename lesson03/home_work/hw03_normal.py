__author__ = 'Вторушин Марк Викторович'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = []
    first_n = 0
    second_n = 1
    for i in range(m + 1):
        if i >= n: a.append(second_n)
        first_n, second_n = second_n, second_n + first_n

    return a
print(fibonacci(1,10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    a = origin_list[:]
    for i in range(1, len(origin_list)):
        n = i
        while (a[n] < a[n - 1]) and (n > 0):
            a[n], a[n - 1] = a[n - 1], a[n]
            n -= 1

    return a
print(sort_to_max([2, 5, 15, 23, 12, 14, 0, 3, 1, 8, 7]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_i(x, y):
    a = []
    for i in y:
        if x(i):
            a.append(i)
    return a

print(filter_i(lambda x:x>=0, [-27, 5, 0, 27, -2, -8, 17]))
print(filter_i(lambda x:x<=0, [-27, 5, 0, 27, -2, -8, 17]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def versh(a1, a2, a3, a4):
    def koord(x, y):
        return ((x[0]+y[0])/2,(x[1]+y[1])/2)
    if a1 == a3 or a2 == a4: return False
    return koord(a1, a3) == koord(a2, a4)
print (versh((2, 5), (3, 7), (1, 2), (4, 3)))
print (versh((5, 0), (7, 1), (2, 1), (0, 0)))
