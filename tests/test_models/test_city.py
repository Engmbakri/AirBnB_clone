#!/usr/bin/python3
"""
City Unittest Module
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """
    Unittests For Instantiation Of The City Class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        mycity = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(mycity))
        self.assertNotIn("state_id", mycity.__dict__)

    def test_name_is_public_class_attribute(self):
        mycity = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(mycity))
        self.assertNotIn("name", mycity.__dict__)

    def test_two_cities_unique_ids(self):
        mycity1 = City()
        mycity2 = City()
        self.assertNotEqual(mycity1.id, mycity2.id)

    def test_two_cities_different_created_at(self):
        mycity1 = City()
        sleep(0.05)
        mycity2 = City()
        self.assertLess(mycity1.created_at, mycity2.created_at)

    def test_two_cities_different_updated_at(self):
        mycity1 = City()
        sleep(0.05)
        mycity2 = City()
        self.assertLess(mycity1.updated_at, mycity2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        mycity = City()
        mycity.id = "024682"
        mycity.created_at = mycity.updated_at = my_date
        mycity_str = mycity.__str__()
        self.assertIn("[City] (024682)", mycity_str)
        self.assertIn("'id': '024682'", mycity_str)
        self.assertIn("'created_at': " + my_date_repr, mycity_str)
        self.assertIn("'updated_at': " + my_date_repr, mycity_str)

    def test_args_unused(self):
        mycity = City(None)
        self.assertNotIn(None, mycity.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        mycity = City(id="345", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(mycity.id, "345")
        self.assertEqual(mycity.created_at, my_date)
        self.assertEqual(mycity.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests For Testing Save Methos Of The City Class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        mycity = City()
        sleep(0.05)
        first_updated_at = mycity.updated_at
        mycity.save()
        self.assertLess(first_updated_at, mycity.updated_at)

    def test_two_saves(self):
        mycity = City()
        sleep(0.05)
        first_updated_at = my_city.updated_at
        mycity.save()
        second_updated_at = mycity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        mycity.save()
        self.assertLess(second_updated_at, mycity.updated_at)

    def test_save_with_arg(self):
        mycity = City()
        with self.assertRaises(TypeError):
            mycity.save(None)

    def test_save_updates_file(self):
        mycity = City()
        mycity.save()
        mycity_id = "City." + mycity.id
        with open("file.json", "r") as f:
            self.assertIn(mycity_id, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests For Testing to_dict Method"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        mycity = City()
        self.assertIn("id", mycity.to_dict())
        self.assertIn("created_at", mycity.to_dict())
        self.assertIn("updated_at", mycity.to_dict())
        self.assertIn("__class__", mycity.to_dict())

    def test_to_dict_contains_added_attributes(self):
        mycity = City()
        mycity.middle_name = "Khartoum"
        mycity.my_number = 777
        self.assertEqual("Khartoum", mycity.middle_name)
        self.assertIn("my_number", mycity.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        mycity = City()
        mycity_dict = mycity.to_dict()
        self.assertEqual(str, type(mycity_dict["id"]))
        self.assertEqual(str, type(mycity_dict["created_at"]))
        self.assertEqual(str, type(mycity_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        mycity = City()
        mycity.id = "024682"
        mycity.created_at = mycity.updated_at = my_date
        to_dict = {
            'id': '024682',
            '__class__': 'City',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(mycity.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        mycity = City()
        self.assertNotEqual(mycity.to_dict(), mycity.__dict__)

    def test_to_dict_with_arg(self):
        mycity = City()
        with self.assertRaises(TypeError):
            mycity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
