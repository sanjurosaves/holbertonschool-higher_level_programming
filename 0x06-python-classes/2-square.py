#!/usr/bin/python3
class Square:
    """square class"""


    def __init__(self, size=0):
        """instantiate"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("sizemust be >=0")
        self.__size = size
