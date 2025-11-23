#!/usr/bin/python3
"""
Module for Pascal's Triangle.
This module provides a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n: The number of rows in the triangle

    Returns:
        list: A list of lists representing Pascal's triangle,
        or empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
