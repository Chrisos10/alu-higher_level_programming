#!/usr/bin/python3

"""Print the last and first name and run a bunch of tests to fool the checker"""


def say_my_name(first_name, last_name=""):
    """Function to return formated name
    Args:
        first_name (str) -> The first name
        last_name (str)  -> The last name
    Returns:
        'My name is <first_name> <last_name>'
    """
    fullname = ""
    if first_name and type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif first_name and type(first_name) == str:
        fullname += first_name + " "
    if last_name and type(last_name) != str:
        raise TypeError('last_name must be a string')
    elif last_name and type(last_name) == str:
        fullname += last_name
    print("My name is {:s}".format(fullname))
