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
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """override __str__ method to return customized string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
