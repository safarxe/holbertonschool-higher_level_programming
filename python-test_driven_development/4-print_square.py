#!/usr/bin/python3
"""
Module for printing squares.
This module provides a function to print a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: Size length of the square (integer)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print(size * "#")