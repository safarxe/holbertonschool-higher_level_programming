#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV data to JSON format and saves it to data.json.

    Args:
        csv_filename: The filename of the CSV file to convert

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False

