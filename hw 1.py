# task 1
# Определить количество четных и нечетных чисел в заданом списке. Оформить в виде функци, где на вход будет подаваться
# список с целыми числами. Результат функции должен быть 2 числа, кол-во четных и нечетных чисел соответственно


def is_an_even_number(number_list=[]):
    even_counter, odd_counter = 0, 0
    for number in number_list:
        if number % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    return even_counter, odd_counter


# task 2
# Написать функцию, которая принемает 2 числа. Функця должна вернуть сумму всех элементов числового ряда между этими
# двумя числами


def sum_of_numbers(number1=0, number2=1):
    result = 0
    number1, number2 = int(number1), int(number2)
    # если числа введены по убыванию
    if number1 > number2:
        number1, number2 = number2, number1
    for number in range(number1, number2 + 1):
        result += number
    return result


# task 3
# Реализовать алгоритм бинарного поиска на python. На вход подается упорядоченный список целых чисел, а также элемент,
# который необходимо найти и указать его индекс, в противном случае - указать что такого элемента нет в заданном списке


def binary_search(number_list, elem_to_search):
    if len(number_list) == 0:
        return 0
    index, minimum, maximum = len(number_list) // 2, 0, len(number_list) - 1
    while maximum >= minimum and number_list[index] != elem_to_search:
        if elem_to_search > number_list[index]:
            minimum = index + 1
        else:
            maximum = index - 1
        index = int((minimum + maximum) / 2)
    else:
        if elem_to_search != number_list[index]:
            return 0
    return index + 1


if __name__ == '__main__':
    # task 1
    assert is_an_even_number([1, 1, 1, 2, 34, 5, 56, 7, 9, 6, 2, 1]) == (5, 7)
    assert is_an_even_number([]) == (0, 0)
    # task 2
    assert sum_of_numbers(1, 5) == 15
    assert sum_of_numbers(4, 1) == 10
    assert sum_of_numbers(1.5, 5.3) == 15
    assert sum_of_numbers() == 1
    # task 3
    print(binary_search([], 2))
    assert binary_search([1, 2, 4, 5, 5, 6], 2) == 2
    assert binary_search([1, 2, 4, 5, 5, 6], 3) == 0
    assert binary_search([1, 2, 4, 5, 5, 6], 6) == 6
    assert binary_search([], 2) == 0
