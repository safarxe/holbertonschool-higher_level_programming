#!/usr/bin/env python3

class SwimMixin:
    """swim mixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """fly mixin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """dragon class"""
    def roar(self):
        print("The dragon roars!")
