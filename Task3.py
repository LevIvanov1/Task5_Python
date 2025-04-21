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

    def test_examine_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_try_one(self):
        self.assertEqual(factorial(1), 1)

    def test_simple_input(self):
        self.assertEqual(factorial(5), 120)

    def test_check_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_boundary_test(self):
        self.assertEqual(factorial(10), 3628800)

    def test_big_number(self):
        with self.assertRaises(ValueError):
            factorial(10000)

    def test_regular_case(self):
        self.assertEqual(factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()