import unittest
from . import hw_6_matrix_counter as hw


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = hw.Matrix

    def tearDown(self):
        print('test finished successfully')

    def test_size(self):
        self.assertEqual(self.matrix([[1, 2, 3, 4], [1, 2, 3, 4]]).size(), (2, 4), 'Wrong size in test 1')
        self.assertEqual(self.matrix([[1, 2], [3, 4], [1, 2], [3, 4]]).size(), (4, 2), 'Wrong size in test 2')
        self.assertEqual(self.matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]).size(), (3, 3), 'Wrong size in test 3')
        self.assertEqual(self.matrix([[1, 2, 3, 4]]).size(), (1, 4), 'Wrong size in test 4')
        self.assertEqual(self.matrix([[1], [2], [3], [4]]).size(), (4, 1), 'Wrong size in test 5')

    def test_mul(self):
        self.assertEqual(self.matrix([[1, 2, 3, 4], [1, 2, 3, 4]]) * 2, [[2, 4, 6, 8], [2, 4, 6, 8]],
                         'Wrong multiply in test 1')
        self.assertEqual(self.matrix([[1, 2], [3, 4], [1, 2], [3, 4]]) * 2, [[2, 4], [6, 8], [2, 4], [6, 8]],
                         'Wrong multiply in test 2')
        self.assertEqual(self.matrix([[1, 2, 3], [1, 2, 3]]) * 2, [[2, 4, 6], [2, 4, 6]], 'Wrong multiply in test 3')
        self.assertEqual(self.matrix([[1, 2, 3, 4]]) * 2, [[2, 4, 6, 8]], 'Wrong multiply in test 4')
        self.assertEqual(self.matrix([[1], [2], [3], [4]]) * 2, [[2], [4], [6], [8]], 'Wrong multiply in test 5')

    def test_add(self):
        self.assertEqual(self.matrix([[1, 2, 3, 4], [1, 2, 3, 4]]) + self.matrix([[2, 4, 6, 8], [2, 4, 6, 8]]),
                         [[3, 6, 9, 12], [3, 6, 9, 12]], 'Wrong add in test 1')
        self.assertEqual(self.matrix([[1, 2], [3, 4], [1, 2], [3, 4]]) + self.matrix([[2, 4], [6, 8], [2, 4], [6, 8]]),
                         [[3, 6], [9, 12], [3, 6], [9, 12]], 'Wrong add in test 2')
        self.assertEqual(self.matrix([[1, 2, 3], [1, 2, 3]]) + self.matrix([[2, 4, 6], [2, 4, 6]]),
                         [[3, 6, 9], [3, 6, 9]], 'Wrong add in test 3')
        self.assertEqual(self.matrix([[1, 2, 3, 4]]) + self.matrix([[2, 4, 6, 8]]), [[3, 6, 9, 12]],
                         'Wrong add in test 4')
        self.assertEqual(self.matrix([[1], [2], [3], [4]]) + self.matrix([[2], [4], [6], [8]]), [[3], [6], [9], [12]],
                         'Wrong add in test 5')
        with self.assertRaisesRegex(hw.MatrixSizeError, 'size'):
            self.matrix([[1, 2, 3, 4], [1, 2, 3, 4]]) + self.matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    def test_get_counter(self):
        self.assertEqual(self.matrix([[1, 2, 3, 4], [1, 2, 3, 4]]).get_counter(), 8, 'Wrong get_counter in test 1')
        self.assertEqual(self.matrix([[1, 2], [3, 4], [1, 2], [3, 4], [1, 2]]).get_counter(), 10,
                         'Wrong get_counter in test 2')
        self.assertEqual(self.matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]).get_counter(), 9, 'Wrong get_counter in test 3')
        self.assertEqual(self.matrix([[1, 2, 3, 4]]).get_counter(), 4, 'Wrong get_counter in test 4')
        self.assertEqual(self.matrix([[1], [2], [3]]).get_counter(), 3, 'Wrong get_counter in test 5')

    def test_transpose(self):
        self.assertEqual(self.matrix([[1, 2, 3, 4], [1, 2, 3, 4]]).transpose(), [[1, 1], [2, 2], [3, 3], [4, 4]],
                         'Wrong transpose in test 1')
        self.assertEqual(self.matrix([[1, 2], [3, 4], [1, 2], [3, 4]]).transpose(), [[1, 3, 1, 3], [2, 4, 2, 4]],
                         'Wrong transpose in test 2')
        self.assertEqual(self.matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]]).transpose(), [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
                         'Wrong transpose in test 3')
        self.assertEqual(self.matrix([[1, 2, 3, 4]]).transpose(), [[1], [2], [3], [4]], 'Wrong transpose in test 4')
        self.assertEqual(self.matrix([[1], [2], [3], [4]]).transpose(), [[1, 2, 3, 4]], 'Wrong transpose in test 5')


if __name__ == '__main__':
    unittest.main()
