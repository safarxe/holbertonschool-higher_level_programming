#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """abstract animal class"""
    @abstractmethod
    def sound(self):
        """return sound of animal"""
        pass


class Dog(Animal):
    """dog class"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """cat class"""
    def sound(self):
        return "Meow"
