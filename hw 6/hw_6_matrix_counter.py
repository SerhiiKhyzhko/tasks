# К реализованному классу Matrix в Домашнем задании 3 добавить следующее:
# 1. __add__ принимающий второй экземпляр класса Matrix и возвращающий сумму матриц, если передалась на вход матрица
# другого размера - поднимать исключение MatrixSizeError (по желанию реализовать так, чтобы текст ошибки содержал
# размерность 1 и 2 матриц - пример: "Matrixes have different sizes - Matrix(x1, y1) and Matrix(x2, y2)")
# 2. __mul__ принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр/
# 3. __str__ переводящий матрицу в строку. Столбцы разделены между собой табуляцией, а строки — переносами
# строк (символ новой строки). При этом после каждой строки не должно быть символа табуляции и в конце не должно быть
# переноса строки.
########################################################################################################################
# 1.Реализовать подсчёт елементов в классе Matrix с помощью collections.Counter.
# Можно реализовать протоколом итератора и тогда будет такой вызов - Counter(maxtrix). Либо сделать какой-то
# метод get_counter(), который будет возвращать объект Counter и подсчитывать все элементы внутри матрицы.
# 2.Используя модуль unittests написать тесты: сложения двух матриц, умножения матрицы и метод transpose

from copy import deepcopy
from collections import Counter
from itertools import chain


class MatrixSizeError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Matrix:
    def __init__(self, list_of_lists: list):
        self.matrix = deepcopy(list_of_lists)

    def size(self) -> tuple:
        return len(self.matrix), len(self.matrix[0])

    def transpose(self):
        self.matrix = [[self.matrix[num][column] for num in range(len(self.matrix))]
                       for column in range(len(self.matrix[0]))]
        return self.matrix

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixSizeError(f'Matrixes have different sizes - Matrix{self.size()} and Matrix{other.size()}')
        add_list = [[x + y for x, y in zip(self.matrix[row], other.matrix[row])] for row in range(len(self.matrix))]
        return add_list
        # return Matrix(add_list)

    def __mul__(self, scalar):
        self.matrix = [[num * scalar for num in row] for row in self.matrix]
        return self.matrix

    def __str__(self):
        my_str = ''
        for row in self.matrix:
            for elem in row:
                my_str += str(elem) + '\t'
            my_str += '\n'
        return my_str

    def get_counter(self):
        return Counter(sum(self.matrix, []))

    @classmethod
    def create_transposed(cls, new_matrix):
        return cls(new_matrix).transpose()
