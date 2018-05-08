#!/usr/bin/python3
class Rectangle():
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """instantiate"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for __width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for __height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
