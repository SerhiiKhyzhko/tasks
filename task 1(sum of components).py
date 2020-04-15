# Написать функцию, которая будет принимать на вход натуральное число n, и возращать сумму его цифр.
# Реализовать используя рекурсию (без циклов, без строк, без контейнерных типов данных).
# Пример: get_sum_of_components(123) -> 6 (1+2+3)


def get_sum_of_components(number):
    if number == 0:
        return 0
    else:
        return number % 10 + get_sum_of_components(int(number / 10))


try:
    number = int(input('Введи число: '))
    # проверка на натуральное число
    if number < 1:
        print('Нужно вводить целые числа больше ноля!!')
    else:
        print(f'сумма составляющих числа {number} равна: {get_sum_of_components(number)}')
except:
    print('Нужно вводить целые числа больше ноля!!')
