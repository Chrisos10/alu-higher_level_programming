#!/usr/bin/python3
"""
a function that prints a square with the character #

size is the size length of the square
"""


def print_square(size):
    """
    size must be an integer, otherwise raise

    a TypeError exception with the message

    size must be an integer

    if size is less than 0, raise a ValueError

    exception with the message size must be >= 0

    if size is a float and is less than 0,

    raise a TypeError exception with the message

    size must be an integer
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
