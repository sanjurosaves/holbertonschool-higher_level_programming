#!/usr/bin/python3

"""creates class Base"""
import json


class Base:
    """ creating Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
