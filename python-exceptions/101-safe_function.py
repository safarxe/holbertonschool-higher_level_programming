#!/usr/bin/python3
# 101-safe_function.py

def safe_function(fct, *args):
    """
    function that executes a function safely.
    """
    import sys
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None

