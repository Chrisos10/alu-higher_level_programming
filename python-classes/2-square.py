#!/usr/bin/python3
"""Defines a square by a private instance attribute 'size'"""


class Square:
    """defining a square"""
    def __init__(self, size=0):
        """
        defines a square
        Attributes:
            size(int): The size of the square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
