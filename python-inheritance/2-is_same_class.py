#!/usr/bin/python3
"""check exact class module"""


def is_same_class(obj, a_class):
    """check if obj is exactly instance of a_class"""
    return type(obj) is a_class
