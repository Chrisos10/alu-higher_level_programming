#!/usr/bin/python3
"""Defines a square by a private instance attribute 'size'"""


class Square:
    """defining a square"""
    def __init__(self, size):
        """
        defines a square
        Attributes:
            size(int): The size of the square
        """
        self.__size = size

