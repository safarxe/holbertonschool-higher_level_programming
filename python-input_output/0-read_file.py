#!/usr/bin/python3
"""
Module for reading text files.
This module provides a function to read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The name of the file to read (default: "")
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
