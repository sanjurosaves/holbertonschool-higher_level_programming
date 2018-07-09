#!/usr/bin/python3
""" creates MyInt rebel class """


class MyInt:
    """ MyInt class """
    def __init__(self, n):
        """ instantiate """
        self.__theint = -n

    def __str__(self):
        """ return string of an opposite universe """
        return "{}".format(-(self.__theint))
