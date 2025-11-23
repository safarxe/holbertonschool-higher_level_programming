#!/usr/bin/python3
"""
Module for appending to text files.
This module provides a function to append a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename: The name of the file to append to (default: "")
        text: The text to append to the file (default: "")

    Returns:
        int: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
