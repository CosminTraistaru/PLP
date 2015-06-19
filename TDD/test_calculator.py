import unittest

from calculator import add


class CalculatorTests(unittest.TestCase):

    def test_returns_0_for_empty_string(self):
        assert add('') == 0

    def test_returns_bare_numbers(self):
        assert add('1') == 1
        assert add('3') == 3

    def test_add_numbers(self):
        assert add('1,2') == 3
        assert add('10,5') == 15

    def test_delimiter(self):
        assert add('1\n2') == 3

    def test_custom(self):
        assert add('cacat1,2') == 3

if __name__ == '__main__':
    unittest.main()