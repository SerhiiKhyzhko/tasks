'''
К реализованному классу Matrix в Домашнем задании 3 добавить следующее:
1. __add__ принимающий второй экземпляр класса Matrix и возвращающий сумму матриц, если передалась на вход матрица
другого размера - поднимать исключение MatrixSizeError (по желанию реализовать так, чтобы текст ошибки содержал
размерность 1 и 2 матриц - пример: "Matrixes have different sizes - Matrix(x1, y1) and Matrix(x2, y2)")
2. __mul__ принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр/
3. __str__ переводящий матрицу в строку. Столбцы разделены между собой табуляцией, а строки — переносами
строк (символ новой строки). При этом после каждой строки не должно быть символа табуляции и в конце не должно быть
переноса строки.
'''

from copy import deepcopy


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
        return Matrix(add_list)

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

    @classmethod
    def create_transposed(cls, new_matr):
        return cls(new_matr).transpose()


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    new_matrix = [[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
    obj = Matrix(matrix)

    another_obj1 = Matrix([[7, 8, 9], [10, 11, 12]])
    another_obj2 = Matrix([[7, 8], [10, 11]])
    assert obj.matrix == [[1, 2, 3], [4, 5, 6]]
    matrix.append([7, 8, 9])
    assert obj.matrix == [[1, 2, 3], [4, 5, 6]]
    assert obj.size() == (2, 3)
    assert obj.transpose() == [[1, 4], [2, 5], [3, 6]]
    assert obj.transpose() == [[1, 2, 3], [4, 5, 6]]
    assert obj.create_transposed(new_matrix) == [[10, 13, 16, 19], [11, 14, 17, 20], [12, 15, 18, 21]]
    assert obj * 2 == [[2, 4, 6], [8, 10, 12]]


