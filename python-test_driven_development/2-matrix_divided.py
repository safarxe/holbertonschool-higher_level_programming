#!/usr/bin/python3
"""
This is the "matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with divided and rounded values."""

    if (not isinstance(matrix, list) or
            not all(isinstance(r, list) for r in matrix) or
            not all(isinstance(n, (int, float)) for r in matrix for n in r)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if len(matrix) == 0:
        raise TypeError("Each row of the matrix must have the same size")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return (new_matrix)