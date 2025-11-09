#!/usr/bin/python3
# 2-matrix_divided.py
"""
Module for dividing matrix elements.
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers or floats
        div: Number (int or float) to divide by

    Returns:
        list: New matrix with divided elements rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of numbers, or rows have different sizes, or div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]

