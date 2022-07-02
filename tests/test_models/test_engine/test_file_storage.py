#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
from os import path
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    This class is an unittest for the instantiation of a FileStorage class
    """

    def test_FileStorage_no_arg(self):
        """Testing for instantiation of FileStorage with no arg"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arg(self):
        """Testing for instantiation of FileStorage with arg"""
        with self.assertRaises(TypeError):
            FileStorage(None)

if __name__ == "__main__":
    unittest.main()