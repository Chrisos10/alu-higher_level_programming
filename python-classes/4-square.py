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
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve"""
        return (self.__size)

    @size.setter
    def size(swlf, value):
         """Setter method to initalize value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square"""
        return (self.__size**2)
