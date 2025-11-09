#!/usr/bin/python3
# 100-safe_print_integer_err.py

def safe_print_integer_err(value):
    """
    function that prints an integer with "{:d}".format().
    """
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False

