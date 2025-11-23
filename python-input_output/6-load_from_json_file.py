#!/usr/bin/python3
"""
Module for loading objects from JSON files.
This module provides a function to create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename: The name of the JSON file to read from

    Returns:
        object: The Python data structure loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
