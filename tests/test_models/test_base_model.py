#!/usr/bin/python3
""" Defines unittest framework for each test suite """
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Unittest initialization for the class area """
    def setUp(self):
        self.real_model = BaseModel()

    def test_initialize(self):
        self.assertIsInstance(self.real_model.id, str)
        self.assertIsInstance(self.real_model.created_at, datetime)
        self.assertIsInstance(self.real_model.updated_at, datetime)

    def test_save_way(self):
        created_at_begin = self.real_model.created_at
        updated_at_update = self.real_model.updated_at

        self.real_model.created_at -= timedelta(seconds=1)
        self.real_model.save()

        self.assertNotEqual(self.real_model.created_at, created_at_begin)
        self.assertGreater(self.real_model.updated_at, updated_at_update)

    def test_to_dict(self):
        new_dict = self.real_model.to_dict()

        self.assertIsInstance(new_dict, dict)
        self.assertIn('__class__', new_dict)
        self.assertEqual(new_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', new_dict)
        self.assertIn('updated_at', new_dict)
        self.assertIn('id', new_dict)

        self.assertEqual(new_dict['id'], self.real_model.id)

        # check if 'id' in new_dict matches the model's id
        self.assertEqual(new_dict['id'], self.real_model.id)

        if __name__ == '__main__':
            unnitest.main()
