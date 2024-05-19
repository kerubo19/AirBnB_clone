#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """

    def test_id(self):
        """
        Test if the 'id' attribute is a string.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at(self):
        """
        Test if 'created_at' is a datetime object.
        """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """
        Test if 'updated_at' is a datetime object.
        """
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save(self):
        """
        Test if 'updated_at' is updated by the save method.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        """
        Test the __str__ method.
        """
        model = BaseModel()
        string = str(model)
        self.assertIn('BaseModel', string)
        self.assertIn(model.id, string)
