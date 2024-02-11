#!/usr/bin/python3
"""
BaseModel Unittest Module
"""
import os
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """
    Unittest For BaseModel
    """

    def setUp(self):
        """
        Temporary File Path Setup
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
        Test for Init
        """
        mymodel = BaseModel()

        self.assertIsNotNone(mymodel.id)
        self.assertIsNotNone(mymodel.created_at)
        self.assertIsNotNone(mymodel.updated_at)

    def test_save(self):
        """
        Test For Save Method
        """
        mymodel = BaseModel()

        initial_updated_at = mymodel.updated_at

        current_updated_at = mymodel.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test For to_dict Method
        """
        mymodel = BaseModel()

        mymodel_dict = mymodel.to_dict()

        self.assertIsInstance(mymodel_dict, dict)

        self.assertEqual(mymodel_dict["__class__"], 'BaseModel')
        self.assertEqual(mymodel_dict['id'], mymodel.id)
        self.assertEqual(mymodel_dict['created_at'],
                         mymodel.created_at.isoformat())
        self.assertEqual(mymodel_dict["updated_at"],
                         mymodel.created_at.isoformat())

    def test_str(self):
        """
        String Representation Test
        """
        mymodel = BaseModel()

        self.assertTrue(str(mymodel).startswith('[BaseModel]'))

        self.assertIn(mymodel.id, str(mymodel))

        self.assertIn(str(mymodel.__dict__), str(mymodel))


if __name__ == "__main__":
    unittest.main()
