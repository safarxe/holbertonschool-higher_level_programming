#!/usr/bin/python3
"""Defines a class Square with size, position, area, printing, and __str__."""


class Square:
    """Represents a square with size, position, area, printing, and __str__."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): Coordinates (x, y) for printing (default (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the private position attribute with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(v, int)
                        for v in value) or
                not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # character and position offsets."""
        if self.__size == 0:
            print()
            return
        # Vertical offset
        for _ in range(self.__position[1]):
            print()
        # Square rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return string representation of the square (same as my_print)."""
        if self.__size == 0:
            return ""
        rows = []
        # Add vertical offset
        for _ in range(self.__position[1]):
            rows.append("")
        # Add square rows
        for _ in range(self.__size):
            rows.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(rows)
