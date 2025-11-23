#!/usr/bin/python3
"""
Module for basic JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        dict: A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

