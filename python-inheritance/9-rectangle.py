#!/usr/bin/python3
"""rectangle class with area and str module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """initialize rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """return string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
