#!/usr/bin/env python3
"""Unittest for User class"""

from datetime import datetime
import unittest
import inspect
import models
from models.user import User
from unittest import mock
from unittest.mock import MagicMock
from time import sleep
import pycodestyle


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on user file"""
    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/user.py'])
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
        self.obj_members(User, inspect.isfunction)

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        msg = "user.py file needs a docstrings"
        self.assertIsNotNone(models.user.__doc__, msg)
        self.assertTrue(len(__doc__) > 0, " user.py have docstrings")
        self.assertFalse(len(__doc__) < 0, " user  have docstrings")


class Test_Class_User(unittest.TestCase):
    """Testing User class"""
    @mock.patch('models.storage')
    def test_User_instance(self, mock_storage):
        instance = User()
        self.assertEqual(type(instance), User)
        self.assertTrue(type(instance) == User)
        self.assertIs(type(instance), User)
        instance.email = "mauricio@ubuntu.com"
        instance.password = "123"
        instance.first_name = "mauricio"
        instance.last_name = "carrasco"
        expectec_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "email": str,
            "password": str,
            "first_name": str,
            "last_name": str
            }
        dict_inst = instance.to_dict()
        expectec_attrs = [
                "id",
                "created_at",
                "updated_at",
                "email",
                "password",
                "first_name",
                "last_name",
                "__class__"]
        self.assertCountEqual(dict_inst.keys(), expectec_attrs)
        self.assertEqual(dict_inst['email'], 'mauricio@ubuntu.com')
        self.assertEqual(dict_inst['password'], "123")
        self.assertEqual(dict_inst['first_name'], 'mauricio')
        self.assertEqual(dict_inst['last_name'], 'carrasco')
        self.assertEqual(dict_inst['__class__'], 'User')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(instance.email, "mauricio@ubuntu.com")
        self.assertEqual(instance.password, "123")
        self.assertEqual(instance.first_name, "mauricio")
        self.assertEqual(instance.last_name, "carrasco")

    def test_datetime(self):
        """
        Test correct datetime assigned of created_at and updated_at
        """
        created_at = datetime.now()
        instance1 = User()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance1.created_at, True)
        self.assertEqual(instance1.created_at <= updated_at, True)
        sleep(0.5)
        created_at = datetime.now()
        instance2 = User()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance2.created_at, True)
        self.assertEqual(instance2.created_at <= updated_at, True)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Testin UUID
        """
        instance1 = User()
        instance2 = User()
        instance3 = User()
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
        instance6 = User()
        us_id = instance6.id
        us_dict = instance6.__dict__
        string_output = "[User] ({}) {}".format(us_id, us_dict)
        self.assertEqual(string_output, str(instance6))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method"""
        instance = User()
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
