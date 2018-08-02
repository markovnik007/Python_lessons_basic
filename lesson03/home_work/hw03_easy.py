__author__ = 'Вторушин Марк Викторович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    sdvig = pow(10, int(ndigits))
    a = number * sdvig
    b = int(a)
    ostatok = a - b
    if not (abs(ostatok) < 0.5):
        if b > 0:
            b += 1
        else:
            b -= 1


    return b / sdvig


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    number = str(ticket_number)
    if len(number) != 6: return False
    oktet_l = 0
    oktet_r = 0
    for i in range(3):
        oktet_l += int(number[i])
        oktet_r += int(number[-i-1])
    return oktet_l == oktet_r


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
