#!/usr/bin/python3
"""check instance or subclass module"""


def is_kind_of_class(obj, a_class):
    """check if obj is instance of a_class or subclass"""
    return isinstance(obj, a_class)
