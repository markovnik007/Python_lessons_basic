__author__ = 'Вторушин Марк Викторович'
# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class worker:
    def __init__(self, name, surname, salary, position, norma):
        self.name = name
        self.surname = surname
        self._salary = int(salary)  # Инкапсулируем
        self.position = position
        self.norma = int(norma)
        self.worked_hours = 0

    def w_hours(self):
        with open('hours_of.txt', 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.worked_hours = int(i.split()[2])
                    break
                else:
                    continue
        # Считаем ЗП
    def sum_salary(self):
        h = self._salary // self.norma
        if self.worked_hours > self.norma:
            raznica = self.worked_hours - self.norma
            salary = (raznica * h) * 2
            return (salary + self._salary)
        elif self.worked_hours < self.norma:
            raznica = self.norma - self.worked_hours
            salary = raznica * h
            return (self._salary - salary)
        else:
            return (self._salary)
        # Метод сбора  преобразованной строкой ЗП
    def w_salary(self, salary):
        with open('ZP.txt', 'a', encoding='UTF-8') as f:
            f.write(self.name + ' ' + self.surname + ' ' + str(salary) + ' ' + self.position)
            f.write('\n')

        # Пишем в файл и разбираем все наши шанешки
def file(file):
    f = open(file, 'r', encoding='UTF-8')
    for i in f.readlines():
        if i.count('Имя') == 1:
            continue
        else:
            name, surname, salary, position, norma = i.split()
            w = worker(name, surname, salary, position, norma)
            w.w_hours()
            salary = w.sum_salary()
            w.w_salary(salary)
    f.close()


file('workers.txt')


