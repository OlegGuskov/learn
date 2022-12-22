# __package__ = '~/py_projects/learn/tests'

from unittest import TestCase, main
from gen_python.guess_numbers import is_valid, input_num, compare_numbers


class GuessNumbersTest(TestCase):

    def test_is_valid0(self):
        self.assertEqual(is_valid('1'), True)
        self.assertNotEqual(is_valid('1'), False)
        self.assertTrue(is_valid('1'))
        self.assertTrue(is_valid('01'))
        self.assertTrue(is_valid('15'))
        self.assertTrue(is_valid('47'))
        self.assertTrue(is_valid('76'))
        self.assertTrue(is_valid('99'))
        self.assertTrue(is_valid('100'))
        self.assertTrue(is_valid('100'))

    def test_is_valid1(self):
        self.assertNotEqual(is_valid("-20"), True)
        self.assertEqual(is_valid("-20"), False)
        self.assertFalse(is_valid("-20"))
        self.assertFalse(is_valid("0"))
        self.assertFalse(is_valid("101"))
        self.assertFalse(is_valid("342"))
        self.assertFalse(is_valid("Aa"))
        self.assertFalse(is_valid("A45"))
        self.assertFalse(is_valid("s6a"))


if __name__ == '__main__':
    main()
