#!/usr/bin/python3
class Square:
    """square class"""

    def __init__(self, size=0):
        """instantiate"""
        self.__size = size

    def area(self):
        """return square area"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size is 0:
            print()
        for x in range(0, self.__size):
            print('#' * self.__size)

    @property
    def size(self):
        """getter for __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for __size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
