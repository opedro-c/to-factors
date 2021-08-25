import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))


from unittest import TestCase, main
from application.to_factors import to_factors


class TestToFactors(TestCase):
    
    def test_number_zero(self):
        self.assertEqual(to_factors(0), [])

    def test_number_one(self):
        self.assertEqual(to_factors(1), [])
    
    def test_number_bigger_than_one(self):
        expected = [2 for c in range(10)]
        self.assertEqual(to_factors(1024), expected)
    
    def test_big_number(self):
        expected = [3, 5, 823]
        self.assertEqual(to_factors(12345), expected)
    
    def test_prime_number(self):
        self.assertEqual(to_factors(13), [13])

    def test_big_prime_number(self):
        self.assertEqual(to_factors(97213), [97213])
    
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            to_factors(-10)

    def test_float_number(self):
        with self.assertRaises(TypeError):
            to_factors(12.0)

    def test_string_as_arg(self):
        with self.assertRaises(TypeError):
            to_factors('Hello')


if __name__ == '__main__':
    main()
