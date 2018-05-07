#!/usr/bin/python3
class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiate"""
        self.__size = size
        self.__position = position

    def area(self):
        """return square area"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size is 0:
            print()
        for z in range(0, self.__position[1]):
            print()
        for x in range(0, self.__size):
            print(' ' * self.__position[0], end='')
            for y in range(0, self.__size):
                print('#', end='')
            print()

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

    @property
    def position(self):
        """getter for __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for __position"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if type(x) is not int or type(y) is not int or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
