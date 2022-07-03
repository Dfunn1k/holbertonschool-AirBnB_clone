#!/usr/bin/python3
"""Unittest for FileStorage class"""
from typing import Type
import unittest
from os import path
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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

    def test_FileStorage_file_path_is_str(self):
        """Testing for type of private class attribute __file_path"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_FileStorage_objects_is_dict(self):
        """Testing for type of private class attribute __file_path"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)


class TestFileStorage_methods(unittest.TestCase):
    """
    This class is an unittest for the methods of a FileStorage class
    """

    def test_all(self):
        """Testing for all method with no arg"""
        self.assertEqual(type(models.storage.all()), dict)

    def test_all_with_arg(self):
        """Testing for all method with arg"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Testing for new method with all models"""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_more_than_1_arg(self):
        """Testing for new method with more than 1 arg"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 10)

    def test_new_None_arg(self):
        """Testing for new method with None arg"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Testing for save method with all models"""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        reader = ""
        with open("file.json", encoding="utf-8") as f:
            reader = f.read()
            self.assertIn("BaseModel." + bm.id, reader)
            self.assertIn("User." + us.id, reader)
            self.assertIn("State." + st.id, reader)
            self.assertIn("Place." + pl.id, reader)
            self.assertIn("City." + ct.id, reader)
            self.assertIn("Amenity." + am.id, reader)
            self.assertIn("Review." + rv.id, reader)

    def test_save_with_arg(self):
        """Testing for save method with arg"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Testing for new method with all models"""
        """Testing for save method with all models"""
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        my_objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, my_objs)
        self.assertIn("User." + us.id, my_objs)
        self.assertIn("State." + st.id, my_objs)
        self.assertIn("Place." + pl.id, my_objs)
        self.assertIn("City." + ct.id, my_objs)
        self.assertIn("Amenity." + am.id, my_objs)
        self.assertIn("Review." + rv.id, my_objs)

    def test_reload_with_arg(self):
        """Testing for reload method with arg"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_no_file(self):
        """Testing for new method with all models"""
        self.assertEqual(None, models.storage.reload())


if __name__ == '__main__':
    unittest.main()
