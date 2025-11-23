#!/usr/bin/python3
"""
Module for pickling custom classes.
"""
import pickle


class CustomObject:
    """
    A custom Python class that can be serialized using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name: A string representing the name
            age: An integer representing the age
            is_student: A boolean indicating if the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.

        Args:
            filename: The filename to save the serialized object to
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an instance from a file using pickle.

        Args:
            filename: The filename to load the serialized object from

        Returns:
            CustomObject: An instance of CustomObject, or None if error
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None

