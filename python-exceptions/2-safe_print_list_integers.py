#!/usr/bin/python3
# 2-safe_print_list_integers.py
def safe_print_list_integers(my_list=[], x=0):
    """
    function that prints the first x elements of a list and only integers.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
    print()
    return count
