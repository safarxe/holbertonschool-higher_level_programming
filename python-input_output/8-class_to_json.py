#!/usr/bin/python3
"""
Module for converting class instances to JSON-serializable dictionaries.
This module provides a function to get dictionary description of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class

    Returns:
        dict: A dictionary containing all attributes of the object
    """
    return obj.__dict__
