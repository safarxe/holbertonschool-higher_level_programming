#!/usr/bin/env python3

class VerboseList(list):
    """list class with notifications"""

    def append(self, item):
        """append with notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """extend with notification"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """remove with notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """pop with notification"""
        if index is None:
            item = self[-1]
            print(f"Popped [{item}] from the list.")
            return super().pop()
        else:
            item = self[index]
            print(f"Popped [{item}] from the list.")
            return super().pop(index)
