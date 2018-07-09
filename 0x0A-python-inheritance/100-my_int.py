#!/usr/bin/python3
""" creates MyInt rebel class """


class MyInt(int):
    """ MyInt class """
    def __eq__(self, yag):
        """ invert eq """
        return int.__ne__(self, yag)

    def __ne__(self, yag):
        """ invert ne """
        return int.__eq__(self, yag)
