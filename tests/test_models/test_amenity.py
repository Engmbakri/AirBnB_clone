#!/usr/bin/python3
"""
Module for Amenity class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests For Testing Instantiation Of The Amenity Class.
    """
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

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amenity_one = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity_one.__dict__)

    def test_two_amenities_unique_ids(self):
        amenity_one = Amenity()
        amenity_two = Amenity()
        self.assertNotEqual(amenity_one.id, amenity_two.id)

    def test_two_amenities_different_created_at(self):
        amenity_one = Amenity()
        sleep(0.05)
        amenity_two = Amenity()
        self.assertLess(amenity_one.created_at, amenity_two.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity_one = Amenity()
        sleep(0.05)
        amenity_two = Amenity()
        self.assertLess(amenity_one.updated_at, amenity_two.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        amenity_one = Amenity()
        amenity_one.id = "777777"
        amenity_one.created_at = amenity_one.updated_at = my_date
        amenity_str = amenity_one.__str__()
        self.assertIn("[Amenity] (777777)", amenity_str)
        self.assertIn("'id': '777777'", amenity_str)
        self.assertIn("'created_at': " + my_date_repr, amenity_str)
        self.assertIn("'updated_at': " + my_date_repr, amenity_str)

    def test_args_unused(self):
        amenity_one = Amenity(None)
        self.assertNotIn(None, amenity_one.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Instantiation With Kwargs Test Method
        """
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        Am = Amenity(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        amenity_one = Am
        self.assertEqual(amenity_one.id, "777")
        self.assertEqual(amenity_one.created_at, my_date)
        self.assertEqual(amenity_one.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """
    Unittests For Save Methods Of The Amenity Class.
    """

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
        amenity_one = Amenity()
        sleep(0.05)
        first_updated_at = amenity_one.updated_at
        amenity_one.save()
        self.assertLess(first_updated_at, amenity_one.updated_at)

    def test_two_saves(self):
        amenity_one = Amenity()
        sleep(0.05)
        first_updated_at = amenity_one.updated_at
        amenity_one.save()
        second_updated_at = amenity_one.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity_one.save()
        self.assertLess(second_updated_at, amenity_one.updated_at)

    def test_save_with_arg(self):
        amenity_one = Amenity()
        with self.assertRaises(TypeError):
            amenity_one.save(None)

    def test_save_updates_file(self):
        amenity_one = Amenity()
        amenity_one.save()
        amenity_id = "Amenity." + amenity_one.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the Amenity class.
    """
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

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amenity_one = Amenity()
        self.assertIn("id", amenity_one.to_dict())
        self.assertIn("created_at", amenity_one.to_dict())
        self.assertIn("updated_at", amenity_one.to_dict())
        self.assertIn("__class__", amenity_one.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amenity_one = Amenity()
        amenity_one.middle_name = "Mohammed"
        amenity_one.my_number = 777
        self.assertEqual("Mohammed", amenity_one.middle_name)
        self.assertIn("my_number", amenity_one.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amenity_one = Amenity()
        amenity_dict = amenity_one.to_dict()
        self.assertEqual(str, type(amenity_dict["id"]))
        self.assertEqual(str, type(amenity_dict["created_at"]))
        self.assertEqual(str, type(amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        amenity_one = Amenity()
        amenity_one.id = "777777"
        amenity_one.created_at = amenity_one.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Amenity',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(amenity_one.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        amenity_one = Amenity()
        self.assertNotEqual(amenity_one.to_dict(), amenity1.__dict__)

    def test_to_dict_with_arg(self):
        amenity_one = Amenity()
        with self.assertRaises(TypeError):
            amenity_one.to_dict(None)


if __name__ == "__main__":
    unittest.main()
