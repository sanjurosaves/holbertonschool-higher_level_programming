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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json string rep of list_objs to file """
        filename = cls.__name__ + ".json"
        list_for_file = []
        if list_objs is not None:
            for obj in list_objs:
                list_for_file.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_for_file))
