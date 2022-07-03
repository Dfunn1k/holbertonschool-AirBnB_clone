#!/usr/bin/env python3
"""Unittest for Review class"""

from datetime import datetime
import unittest
import inspect
import models
from models.review import Review
from unittest import mock
from unittest.mock import MagicMock
from time import sleep
import pycodestyle


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on review file"""
    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/review.py'])
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
        self.obj_members(Review, inspect.isfunction)

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        msg = "review.py file needs a docstrings"
        self.assertIsNotNone(models.review.__doc__, msg)
        self.assertTrue(len(__doc__) > 0, " review.py have docstrings")
        self.assertFalse(len(__doc__) < 0, " review  have docstrings")


class Test_Class_Review(unittest.TestCase):
    """Testing Review class"""
    @mock.patch('models.storage')
    def test_Review_instance(self, mock_storage):
        instance = Review()
        self.assertEqual(type(instance), Review)
        self.assertTrue(type(instance) == Review)
        self.assertIs(type(instance), Review)
        instance.place_id = "12-34"
        instance.user_id = "10-50-20"
        instance.text = "5 stars!"
        expectec_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "place_id": str,
            "user_id": str,
            "text": str,
            }
        dict_inst = instance.to_dict()
        expectec_attrs = [
                "id",
                "created_at",
                "updated_at",
                "place_id",
                "user_id",
                "text",
                "__class__"]
        self.assertCountEqual(dict_inst.keys(), expectec_attrs)
        self.assertEqual(dict_inst['place_id'], '12-34')
        self.assertEqual(dict_inst['user_id'], '10-50-20')
        self.assertEqual(dict_inst['text'], '5 stars!')
        self.assertEqual(dict_inst['__class__'], 'Review')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(instance.place_id, "12-34")
        self.assertEqual(instance.user_id, "10-50-20")
        self.assertEqual(instance.text, "5 stars!")

    def test_datetime(self):
        """
        Test correct datetime assigned of created_at and updated_at
        """
        created_at = datetime.now()
        instance1 = Review()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance1.created_at, True)
        self.assertEqual(instance1.created_at <= updated_at, True)
        sleep(0.5)
        created_at = datetime.now()
        instance2 = Review()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance2.created_at, True)
        self.assertEqual(instance2.created_at <= updated_at, True)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Testin UUID
        """
        instance1 = Review()
        instance2 = Review()
        instance3 = Review()
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
        instance6 = Review()
        rv_id = instance6.id
        rv_dict = instance6.__dict__
        string_output = "[Review] ({}) {}".format(rv_id, rv_dict)
        self.assertEqual(string_output, str(instance6))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method"""
        instance = Review()
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
