#!/usr/bin/python3
""" creates Square class, inheriting from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class is inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ instantiate square """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for size """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__size = value

    def __str__(self):
        """override __str__ method to return customized string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
