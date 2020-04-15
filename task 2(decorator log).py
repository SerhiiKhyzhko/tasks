# Написать декоратор log, который будет выводить на экран все аргументы, которые передаются вызываемой функции.
# @log
# def my_sum(*args):
# return sum(*args)

# my_sum(1,2,3,1) - выведет "Функция была вызвана с - 1, 2, 3, 1"
# my_sum(22, 1) - выведет "Функция была вызвана с - 22, 1"


def log(func):
    def wrapper(*args):
        print('Функция была вызвана с - ', end='')
        print(*args, sep=',')

    return wrapper


@ log
def my_sum(*args):
    return sum(*args)


my_sum(1, 2, 3, 1)

