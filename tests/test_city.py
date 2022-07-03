#!/usr/bin/python3
"""Unittest for City class"""

from datetime import datetime
import unittest
import inspect
import models
from models.city import City
from unittest import mock
from unittest.mock import MagicMock
from time import sleep
import pycodestyle


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on city file"""
    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/city.py'])
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
        self.obj_members(City, inspect.isfunction)

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        msg = "city.py file needs a docstrings"
        self.assertIsNotNone(models.city.__doc__, msg)
        self.assertTrue(len(__doc__) > 0, " city.py have docstrings")
        self.assertFalse(len(__doc__) < 0, " city  have docstrings")


class Test_Class_City(unittest.TestCase):
    """Testing City class"""
    @mock.patch('models.storage')
    def test_City_instance(self, mock_storage):
        instance = City()
        self.assertEqual(type(instance), City)
        self.assertTrue(type(instance) == City)
        self.assertIs(type(instance), City)
        instance.state_id = "4210"
        instance.name = "San Francisco"
        expectec_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "state_id": str,
            "name": str
            }
        dict_inst = instance.to_dict()
        expectec_attrs = [
                "id",
                "created_at",
                "updated_at",
                "state_id",
                "name",
                "__class__"]
        self.assertCountEqual(dict_inst.keys(), expectec_attrs)
        self.assertEqual(dict_inst['state_id'], '4210')
        self.assertEqual(dict_inst['name'], 'San Francisco')
        self.assertEqual(dict_inst['__class__'], 'City')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(instance.state_id, "4210")
        self.assertEqual(instance.name, "San Francisco")

    def test_datetime(self):
        """
        Test correct datetime assigned of created_at and updated_at
        """
        created_at = datetime.now()
        instance1 = City()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance1.created_at, True)
        self.assertEqual(instance1.created_at <= updated_at, True)
        sleep(0.5)
        created_at = datetime.now()
        instance2 = City()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance2.created_at, True)
        self.assertEqual(instance2.created_at <= updated_at, True)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Testin UUID
        """
        instance1 = City()
        instance2 = City()
        instance3 = City()
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
        instance6 = City()
        ct_id = instance6.id
        ct_dict = instance6.__dict__
        string_output = "[City] ({}) {}".format(ct_id, ct_dict)
        self.assertEqual(string_output, str(instance6))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method"""
        instance = City()
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
