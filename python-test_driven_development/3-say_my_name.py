#!/usr/bin/python3

"""Print the last and first name and run a bunch of tests"""


def say_my_name(first_name, last_name=""):
    """Function to return formated name
    Args:
        first_name (str) -> The first name
        last_name (str)  -> The last name
    Returns:
        'My name is <first_name> <last_name>'
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

