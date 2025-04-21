import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class Testing(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_simple(self):
        self.assertEqual(factorial(5), 120)

    def test_checkMunis(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_boundary(self):
        self.assertEqual(factorial(10), 3628800)

    def test_bigNumber(self):
        with self.assertRaises(ValueError):
            factorial(10000)

    def test_regularCase(self):
        self.assertEqual(factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()