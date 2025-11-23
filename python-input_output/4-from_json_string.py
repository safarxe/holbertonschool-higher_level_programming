#!/usr/bin/python3
"""
Module for JSON deserialization.
This module provides a function to convert JSON strings to Python objects.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to deserialize

    Returns:
        object: The Python data structure represented by the JSON string
    """
    return json.loads(my_str)
