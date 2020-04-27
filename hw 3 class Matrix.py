'''
Реализовать некий класс Matrix, у которого:
1. Есть собственный конструктор, который принимает в качестве аргумента - список списков, копирует его
(то есть при изменении списков, значения в экземпляре класса не должны меняться).
Элементы списков гарантированно числа, и не пустые.
2. Метод size без аргументов, который возвращает кортеж вида (число строк, число столбцов).
3. Метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)
4. На основе пункта 3 сделать метод класса create_transposed, который будет принимать на вход список списков, как и в
пункте 1, но при этом создавать сразу транспонированную матрицу.
Псевдо код(параметры функций упущены):
class Matrix:
def __init__()
pass

def size():
pass

def transpose():
pass

@classmethod
def create_transposed():
pass
'''
from copy import deepcopy


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def transpose(self):
        self.matrix = [[self.matrix[number][column] for number in range(len(self.matrix))]
                       for column in range(len(self.matrix[0]))]
        return self.matrix


    @classmethod
    def create_transposed(cls, new_matr):
        return cls(new_matr).transpose()


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    new_matrix = [[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
    obj = Matrix(matrix)
    matrix.append([7, 8, 9])
    assert obj.matrix == [[1, 2, 3], [4, 5, 6]]
    assert obj.size() == (2, 3)
    assert obj.transpose() == [[1, 4], [2, 5], [3, 6]]
    assert obj.transpose() == [[1, 2, 3], [4, 5, 6]]
    assert obj.create_transposed(new_matrix) == [[10, 13, 16, 19], [11, 14, 17, 20], [12, 15, 18, 21]]
