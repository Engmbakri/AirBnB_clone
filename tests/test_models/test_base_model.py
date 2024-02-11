#!/usr/bin/python3
"""
BaseModel Unittest
"""
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBasemodel(unittest.TestCase):
    """
    Unittest For BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        Test for init
        """
        mymodel = BaseModel()

        self.assertIsNotNone(mymodel.id)
        self.assertIsNotNone(mymodel.created_at)
        self.assertIsNotNone(mymodel.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        mymodel = BaseModel()

        initial_updated_at = mymodel.updated_at

        current_updated_at = mymodel.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        mymodel = BaseModel()
        mymodel_dict = mymodel.to_dict()
        self.assertIsInstance(mymodel_dict, dict)
        self.assertEqual(mymodel_dict["__class__"], 'BaseModel')
        self.assertEqual(mymodel_dict['id'], mymodel.id)
        self.assertEqual(mymodel_dict['created_at'],
                         mymodel.created_at.isoformat())
        updated_at_datetime = datetime.strptime(mymodel_dict["updated_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated_at_datetime, mymodel.updated_at)

    def test_str(self):
        """
        string representation
        """
        mymodel = BaseModel()

        self.assertTrue(str(mymodel).startswith('[BaseModel]'))

        self.assertIn(mymodel.id, str(mymodel))

        self.assertIn(str(mymodel.__dict__), str(mymodel))


if __name__ == "__main__":
    unittest.main()
