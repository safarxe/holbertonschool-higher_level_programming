#!/usr/bin/python3
"""mylist class module"""


class MyList(list):
    """mylist class that inherits from list"""

    def print_sorted(self):
        """print list in ascending order"""
        print(sorted(self))
