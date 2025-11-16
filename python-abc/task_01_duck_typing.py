#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method for perimeter"""
        pass


class Circle(Shape):
    """circle class"""

    def __init__(self, radius):
        """initialize circle with radius"""
        self.__radius = abs(radius)

    def area(self):
        """calculate circle area"""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """calculate circle perimeter"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """rectangle class"""

    def __init__(self, width, height):
        """initialize rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """calculate rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate rectangle perimeter"""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """print area and perimeter"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
