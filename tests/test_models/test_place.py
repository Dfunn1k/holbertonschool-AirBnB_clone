#!/usr/bin/env python3
"""Unittest for Place class"""

from datetime import datetime
import unittest
import inspect
import models
from models.place import Place
from unittest import mock
from unittest.mock import MagicMock
from time import sleep
import pycodestyle


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on place file"""
    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/place.py'])
        msg = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, msg)


class Test_docstrings(unittest.TestCase):
    """Test docstrings"""
    @classmethod
    def setup_class(self):
        """
        inspect.getmembers(object, [predicate])
        Return all the members of an object in a list of (name, value)
        pairs sorted by name
        only members for which the predicate returns a true value are included
        """
        self.obj_members(Place, inspect.isfunction)

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        msg = "place.py file needs a docstrings"
        self.assertIsNotNone(models.place.__doc__, msg)
        self.assertTrue(len(__doc__) > 0, " place.py have docstrings")
        self.assertFalse(len(__doc__) < 0, " place  have docstrings")


class Test_Class_Place(unittest.TestCase):
    """Testing Place class"""
    @mock.patch('models.storage')
    def test_Place_instance(self, mock_storage):
        instance = Place()
        self.assertEqual(type(instance), Place)
        self.assertTrue(type(instance) == Place)
        self.assertIs(type(instance), Place)
        instance.city_id = "4210"
        instance.user_id = "10-50-20"
        instance.name = "Silicon Valley Place"
        instance.description = "Center of innovation"
        instance.number_rooms = 4
        instance.number_bathrooms = 4
        instance.max_guest = 10
        instance.price_by_night = 100
        instance.latitude = 37.7749
        instance.longitude = 122.4194
        instance.amenity_ids = ["12", "13", "14"]
        expectec_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "city_id": str,
            "user_id": str,
            "name": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list
            }
        dict_inst = instance.to_dict()
        expectec_attrs = [
                "id",
                "created_at",
                "updated_at",
                "city_id",
                "user_id",
                "name",
                "description",
                "number_rooms",
                "number_bathrooms",
                "max_guest",
                "price_by_night",
                "latitude",
                "longitude",
                "amenity_ids",
                "__class__"]
        self.assertCountEqual(dict_inst.keys(), expectec_attrs)
        self.assertEqual(dict_inst['city_id'], '4210')
        self.assertEqual(dict_inst['user_id'], '10-50-20')
        self.assertEqual(dict_inst['name'], 'Silicon Valley Place')
        self.assertEqual(dict_inst['description'], 'Center of innovation')
        self.assertEqual(dict_inst['number_rooms'], 4)
        self.assertEqual(dict_inst['number_bathrooms'], 4)
        self.assertEqual(dict_inst['max_guest'], 10)
        self.assertEqual(dict_inst['price_by_night'], 100)
        self.assertEqual(dict_inst['latitude'], 37.7749)
        self.assertEqual(dict_inst['longitude'], 122.4194)
        self.assertEqual(dict_inst['amenity_ids'], ['12', '13', '14'])
        self.assertEqual(dict_inst['__class__'], 'Place')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(instance.city_id, "4210")
        self.assertEqual(instance.user_id, "10-50-20")
        self.assertEqual(instance.name, "Silicon Valley Place")
        self.assertEqual(instance.description, "Center of innovation")
        self.assertEqual(instance.number_rooms, 4)
        self.assertEqual(instance.number_bathrooms, 4)
        self.assertEqual(instance.max_guest, 10)
        self.assertEqual(instance.price_by_night, 100)
        self.assertEqual(instance.latitude, 37.7749)
        self.assertEqual(instance.longitude, 122.4194)
        self.assertEqual(instance.amenity_ids, ['12', '13', '14'])

    def test_datetime(self):
        """
        Test correct datetime assigned of created_at and updated_at
        """
        created_at = datetime.now()
        instance1 = Place()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance1.created_at, True)
        self.assertEqual(instance1.created_at <= updated_at, True)
        sleep(0.5)
        created_at = datetime.now()
        instance2 = Place()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance2.created_at, True)
        self.assertEqual(instance2.created_at <= updated_at, True)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Testin UUID
        """
        instance1 = Place()
        instance2 = Place()
        instance3 = Place()
        list_instances = [instance1, instance2, instance3]
        for instance in list_instances:
            ins_uuid = instance.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Testing returns STR method"""
        instance6 = Place()
        pl_id = instance6.id
        pl_dict = instance6.__dict__
        string_output = "[Place] ({}) {}".format(pl_id, pl_dict)
        self.assertEqual(string_output, str(instance6))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method"""
        instance = Place()
        created_ats = instance.created_at
        sleep(0.5)
        updated_ats = instance.updated_at
        instance.save()
        saved_inst = instance.created_at
        sleep(0.5)
        updated_inst = instance.updated_at
        self.assertNotEqual(updated_ats, updated_inst)
        self.assertEqual(created_ats, saved_inst)
        self.assertTrue(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main()
