#!/usr/bin/python3
"""square class with custom str module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate square area"""
        return self.__size * self.__size

    def __str__(self):
        """return string representation"""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
