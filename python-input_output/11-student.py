#!/usr/bin/python3
"""
Module for Student class with JSON serialization and deserialization.
This module defines a Student class with save/load capabilities.
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name: The first name of the student
        last_name: The last name of the student
        age: The age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name: The first name of the student
            last_name: The last name of the student
            age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: A list of strings representing attribute names to include.
                   If None, all attributes are included.

        Returns:
            dict: A dictionary containing the student's attributes
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json: A dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
