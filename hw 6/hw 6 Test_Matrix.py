import unittest
from . import hw_6_matrix_counter as hw


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = hw.Matrix
        self.matr1 = [[1, 2, 3, 4], [1, 2, 3, 4]]
        self.matr2 = [[1, 2], [3, 4], [1, 2], [3, 4]]
        self.matr3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        self.matr4 = [[1, 2, 3, 4]]
        self.matr5 = [[1], [2], [3], [4]]

    def tearDown(self):
        print('=============================================================================')

    def test_size(self):
        self.assertEqual(self.matrix(self.matr1).size(), (2, 4), 'Wrong size in test 1')
        self.assertEqual(self.matrix(self.matr2).size(), (4, 2), 'Wrong size in test 2')
        self.assertEqual(self.matrix(self.matr3).size(), (3, 3), 'Wrong size in test 3')
        self.assertEqual(self.matrix(self.matr4).size(), (1, 4), 'Wrong size in test 4')
        self.assertEqual(self.matrix(self.matr5).size(), (4, 1), 'Wrong size in test 5')
        print('size tests finished successfully')

    def test_mul(self):
        self.assertEqual(self.matrix(self.matr1) * 2, [[2, 4, 6, 8], [2, 4, 6, 8]],
                         'Wrong multiply in test 1')
        self.assertEqual(self.matrix(self.matr2) * 2, [[2, 4], [6, 8], [2, 4], [6, 8]],
                         'Wrong multiply in test 2')
        self.assertEqual(self.matrix(self.matr3) * 2, [[2, 4, 6], [2, 4, 6]], 'Wrong multiply in test 3')
        self.assertEqual(self.matrix(self.matr4) * 2, [[2, 4, 6, 8]], 'Wrong multiply in test 4')
        self.assertEqual(self.matrix(self.matr5) * 2, [[2], [4], [6], [8]], 'Wrong multiply in test 5')
        print('mul tests finished successfully')

    def test_add(self):
        self.assertEqual(self.matrix(self.matr1) + self.matrix([[2, 4, 6, 8], [2, 4, 6, 8]]),
                         [[3, 6, 9, 12], [3, 6, 9, 12]], 'Wrong add in test 1')
        self.assertEqual(self.matrix(self.matr2) + self.matrix([[2, 4], [6, 8], [2, 4], [6, 8]]),
                         [[3, 6], [9, 12], [3, 6], [9, 12]], 'Wrong add in test 2')
        self.assertEqual(self.matrix(self.matr3) + self.matrix([[2, 4, 6], [2, 4, 6]]),
                         [[3, 6, 9], [3, 6, 9]], 'Wrong add in test 3')
        self.assertEqual(self.matrix(self.matr4) + self.matrix([[2, 4, 6, 8]]), [[3, 6, 9, 12]],
                         'Wrong add in test 4')
        self.assertEqual(self.matrix(self.matr5) + self.matrix([[2], [4], [6], [8]]), [[3], [6], [9], [12]],
                         'Wrong add in test 5')
        with self.assertRaisesRegex(hw.MatrixSizeError, 'size'):
            self.matrix(self.matr1) + self.matrix(self.matr2)
        print('add tests finished successfully')

    def test_transpose(self):
        self.assertEqual(self.matrix(self.matr1).transpose(), [[1, 1], [2, 2], [3, 3], [4, 4]],
                         'Wrong transpose in test 1')
        self.assertEqual(self.matrix(self.matr2).transpose(), [[1, 3, 1, 3], [2, 4, 2, 4]],
                         'Wrong transpose in test 2')
        self.assertEqual(self.matrix(self.matr3).transpose(), [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
                         'Wrong transpose in test 3')
        self.assertEqual(self.matrix(self.matr4).transpose(), [[1], [2], [3], [4]], 'Wrong transpose in test 4')
        self.assertEqual(self.matrix(self.matr5).transpose(), [[1, 2, 3, 4]], 'Wrong transpose in test 5')
        print('transpose tests finished successfully')


if __name__ == '__main__':
    unittest.main()
