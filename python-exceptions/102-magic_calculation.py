#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(a, b):
    """
    function that does exactly the same as the Python bytecode.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result

