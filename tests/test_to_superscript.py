import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))


from unittest import TestCase, main
from application.to_factors import to_superscript


class TestSuperscript(TestCase):

    def test_zero(self):
        self.assertEqual(to_superscript(0), '⁰')

    def test_even_number(self):
        self.assertEqual(to_superscript(8), '⁸')

    def test_odd_number(self):
        self.assertEqual(to_superscript(1111), '¹¹¹¹')

    def test_number_10(self):
        self.assertEqual(to_superscript(10), '¹⁰')
    
    def test_multiple_of_10(self):
        self.assertEqual(to_superscript(1000), '¹⁰⁰⁰')

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            to_superscript(-1000)
    
    def test_float_number(self):
        with self.assertRaises(TypeError):
            to_superscript(10.2)
    
    def test_string_as_arg(self):
        with self.assertRaises(TypeError):
            to_superscript('Hi')


if __name__ == '__main__':
    main()
