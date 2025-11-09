#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_positive_numbers(self):
        """Test with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        """Test with single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 2, 3, 3]), 3)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_mixed_int_float(self):
        """Test with mixed int and float"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        self.assertEqual(max_integer([1.5, 2, 3.5]), 3.5)


if __name__ == '__main__':
    unittest.main()

