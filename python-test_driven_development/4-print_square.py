#!/usr/bin/python3
"""
A function that prints a square with the character #
Run tests for invalid inputs and raise error
"""


def print_square(size):
    """ Function to print squares of '#'
    Args:
        size(int/float) -> number of "#"'s to print
                        -> Must be an int or a float >= 0
    Returns nothing except if an exception occured,
    in which case the exception raised is returned
    """
    try:
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        char = ""
        for i in range(size):
            for _ in range(size):
                char += '#'
            if i != size - 1:
                char += '\n'
        if size == 0:
            return print(end="")
        else:
            return print(char)
    except TypeError:
        raise
    except ValueError:
        raise
    except OverflowError:
        raise
