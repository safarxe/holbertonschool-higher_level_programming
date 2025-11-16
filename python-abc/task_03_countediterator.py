#!/usr/bin/env python3

class CountedIterator:
    """iterator that tracks count"""

    def __init__(self, iterable):
        """initialize iterator"""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """get next item"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """return count"""
        return self.count
