#!/usr/bin/python3
""" test Base class """
import pep8
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseMethods(unittest.TestCase):
    """class with tests"""

    def test_check_id(self):
        """checking that id is correct - should return false"""
        r1 = Base()
        self.assertEqual(r1.id, 1)
        r2 = Base(12)
        self.assertEqual(r2.id, 12)
        r3 = Base()
        self.assertEqual(r3.id, 2)
        r4 = Base(-9)
        self.assertEqual(r4.id, -9)
