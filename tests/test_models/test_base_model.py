#!/usr/bin/python3
""" This module defines unittest for models/tests/test_model.py """
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelVariable(unittest.TestCase):
    """ Testing from the top of the class BaseModel """

    def test_non_variable(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_updation(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_attribute(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_time_at_creation(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_at_updation(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_class(self):
        spot_one = BaseModel()
        sleep(0.05)
        spot_two = BaseModel()
        self.assertLess(spot_one.updated_at, spot_two.updated_at)

    def test_repping(self):
        dtp = datetime.today()
        date_repping = repr(dtp)
        model_be = BaseModel()
        model_be.id = "689012"
        model_be.created_at = model_be.updated_at = dtp
        model_bestr = model_be.__str__()
        self.assertIn("[BaseModel] (689012)", model_bestr)
        self.assertIn("'id': '689012'", model_bestr)
        self.assertIn("'created_at': " + date_repping, model_bestr)
        self.assertIn("'updated_at': " + date_repping, model_bestr)

    def test_non_variable_with_none(self):
        model_be = BaseModel(None)
        self.assertNotIn(None, model_be.__dict__.values())

    def test_vars(self):
        dtp = datetime.today()
        dtp_iso = dtp.isoformat()
        model_be = BaseModel(id="406", created_at=dtp_iso, updated_at=dtp_iso)
        self.assertEqual(model_be.id, "406")
        self.assertEqual(model_be.created_at, dtp)
        self.assertEqual(model_be.updated_at, dtp)


class TestBaseModelSave(unittest.TestCase):
    """Testing the save method of the BaseModel class."""

    @classmethod
    def set_neccessary_Up(cls):
        try:
            os.rename("file.json", "my_back_ups")
        except IOError:
            pass

    @classmethod
    def tearDown(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("my_back_ups", "file.json")
        except IOError:
            pass

    def test_saving_point(self):
        model_be = BaseModel()
        sleep(0.05)
        starting_updated_at = model_be.updated_at
        model_be.save()
        ending_updated_at = model_be.updated_at
        self.assertLess(starting_updated_at, ending_updated_at)
        sleep(0.05)
        model_be.save()
        self.assertLess(ending_updated_at, model_be.updated_at)

    def test_save_dico(self):
        model_be = BaseModel()
        model_be.save()
        model_beid = "BaseModel." + model_be.id
        with open("file.json", "r") as f:
            self.assertIn(model_beid, f.read())


class TestBaseModelToDict(unittest.TestCase):
    def test_to_dict_type(self):
        model_be = BaseModel()
        self.assertTrue(dict, type(model_be.to_dict()))

    def test_for_right_keys(self):
        model_be = BaseModel()
        self.assertIn("id", model_be.to_dict())
        self.assertIn("created_at", model_be.to_dict())
        self.assertIn("updated_at", model_be.to_dict())
        self.assertIn("__class__", model_be.to_dict())

    def test_to_dict_elements(self):
        model_be = BaseModel()
        model_be.name = "Chicago"
        model_be.my_number = 64
        self.assertIn("name", model_be.to_dict())
        self.assertIn("my_number", model_be.to_dict())

    def test_to_dict_element(self):
        model_be = BaseModel()
        model_be_dict = model_be.to_dict()
        self.assertEqual(str, type(model_be_dict["created_at"]))
        self.assertEqual(str, type(model_be_dict["updated_at"]))

    def test_to_dict_resulting(self):
        dtp = datetime.today()
        model_be = BaseModel()
        model_be.id = "123456"
        model_be.created_at = model_be.updated_at = dtp

        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dtp.isoformat(),
            'updated_at': dtp.isoformat()
        }
        self.assertDictEqual(model_be.to_dict(), expected_dict)

    def test_another_to_dict_blunt(self):
        model_be = BaseModel()
        self.assertNotEqual(model_be.to_dict(), model_be.__dict__)

    def test_to_dict_at_var(self):
        model_be = BaseModel()
        with self.assertRaises(TypeError):
            model_be.to_dict(None)


if __name__ == "__main__":
    unittest.main()
