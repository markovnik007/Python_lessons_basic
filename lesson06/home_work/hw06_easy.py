__author__ = 'Вторушин Марк Викторович'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math
# Создаем класс "треугольник"
class triangle():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        # Вычисляем стороны треугольника по заданным координатам
        self.a = round(math.sqrt(int(math.fabs(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))), 2)
        self.b = round(math.sqrt(int(math.fabs(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))), 2)
        self.c = round(math.sqrt(int(math.fabs(((x1 - x3) ** 2) + ((y1 - y3) ** 2)))), 2)
    # Вычисляем периметр путем сложения сторон
    def perimeter(self):
        self.perimeter = (self.a + self.b + self.c)
        return self.perimeter
    # Вычисляем площадь треугольника по формуле Герона (Так быстрее и проще, тем более посчитали периметр)
    def area(self):
        self.area = self.perimeter / 2
        return self.area
    # Вычисляем высоту треугольника через площадь и основание
    def high(self):
        self.high = self.area * 2 / self.c
        return self.high

# Задаем координаты вершин треугольника (интереснее бы было если бы программа просила задать координаты)
triangle_calc = triangle(2,3,3,6,4,8)
# Выводим все, что нашли через format
print('Длины сторон a = {}, b = {}, c = {}'.format(triangle_calc.a, triangle_calc.b, triangle_calc.c))
print('Значение периметра треугольника {}'.format(triangle_calc.perimeter()))
print('Значение площади треугольника {}'.format(triangle_calc.area()))
print('Высота треугольника {}'.format(triangle_calc.high()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Создаем класс "трапеция"
class trapeze():
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        # Находим стороны трапеции
   # def abcd(self):
        self.a = round(math.sqrt(int(math.fabs(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))), 2)
        self.b = round(math.sqrt(int(math.fabs(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))), 2)
        self.c = round(math.sqrt(int(math.fabs(((x4 - x3) ** 2) + ((y4 - y3) ** 2)))), 2)
        self.d = round(math.sqrt(int(math.fabs(((x1 - x4) ** 2) + ((y1 - y4) ** 2)))), 2)
    #    return self.a, self.b, self.c, self.d
        # Проводим проверку является ли фигура равнобочной трапецией
    def trapeze_test(self):
        if self.b == self.d and self.a != self.c or self.b != self.d and self.a == self.c:
            print("Трапеция равнобедренная!")
        else:                                       # Не пойму откуда у меня None лезет
            print("Трапеция не равнобедренная!")
        # Вычисляем периметр трапеции
    def perimeter(self):
        self.perimeter = (self.a + self.b + self.c + self.d)
        return self.perimeter
        # Вычисляем площадь трапеции по формуле (ОБОГИ!)))) Б-р-а-х-м-а-г-у-п-т-ы
    def area(self):
        self.area = (self.a + self.b) / 2 * \
                    (math.sqrt(int(self.c**2-(((self.b - self.a)**2+self.c**2-self.d**2))/2*(self.a-self.b))**2))
        return self.area

trapeze_calc = trapeze(1,3,4,1,2,3,4,6)

print('Длины сторон a = {}, b = {}, c = {}, d = {}'.format(trapeze_calc.a, trapeze_calc.b,
                                                           trapeze_calc.c, trapeze_calc.d))
print(trapeze.trapeze_test(trapeze_calc))   # Помоему я тут что то завернул)))
print('Значение периметра трапеции {}'.format(trapeze_calc.perimeter()))
print("Значение площади трапеции {}".format(trapeze_calc.area()))