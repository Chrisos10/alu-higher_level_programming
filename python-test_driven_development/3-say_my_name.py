#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>

Run tests and raise TypeError in case of invalid inputs
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must be strings otherwise,

    raise a TypeError exception with the message first_name

    must be a string or last_name must be a string
    """
    try:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        elif not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
    except TypeError:
        raise
    else:
        return print("My name is {} {}".format(first_name, last_name))

