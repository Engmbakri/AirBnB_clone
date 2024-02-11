#!/usr/bin/python3
"""
Place Class Unittest Module
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests For Testing Instantiation Of Place Class.
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
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(myplace))
        self.assertNotIn("city_id", myplace.__dict__)

    def test_user_id_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(myplace))
        self.assertNotIn("user_id", myplace.__dict__)

    def test_name_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(myplace))
        self.assertNotIn("name", myplace.__dict__)

    def test_description_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(myplace))
        self.assertNotIn("desctiption", myplace.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(myplace))
        self.assertNotIn("number_rooms", myplace.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(myplace))
        self.assertNotIn("number_bathrooms", myplace.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(myplace))
        self.assertNotIn("max_guest", myplace.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(myplace))
        self.assertNotIn("price_by_night", myplace.__dict__)

    def test_latitude_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(myplace))
        self.assertNotIn("latitude", myplace.__dict__)

    def test_longitude_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(myplace))
        self.assertNotIn("longitude", myplace.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        myplace = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(myplace))
        self.assertNotIn("amenity_ids", myplace.__dict__)

    def test_two_places_unique_ids(self):
        myplace_one = Place()
        myplace_two = Place()
        self.assertNotEqual(myplace_one.id, myplace_two.id)

    def test_two_places_different_created_at(self):
        myplace_one = Place()
        sleep(0.05)
        myplace_two = Place()
        self.assertLess(myplace_one.created_at, myplace_two.created_at)

    def test_two_places_different_updated_at(self):
        myplace_one = Place()
        sleep(0.05)
        myplace_two = Place()
        self.assertLess(myplace_one.updated_at, myplace_two.updated_at)

    def test_str_representation(self):
        mydate = datetime.today()
        mydate_repr = repr(mydate)
        myplace = Place()
        myplace.id = "666666"
        myplace.created_at = myplace.updated_at = mydate
        myplace_str = myplace.__str__()
        self.assertIn("[Place] (666666)", myplace_str)
        self.assertIn("'id': '666666'", myplace_str)
        self.assertIn("'created_at': " + mydate_repr, myplace_str)
        self.assertIn("'updated_at': " + mydate_repr, myplace_str)

    def test_args_unused(self):
        myplace = Place(None)
        self.assertNotIn(None, myplace.__dict__.values())

    def test_instantiation_with_kwargs(self):
        mydate = datetime.today()
        mydate_iso = mydate.isoformat()
        Pl = Place(id="666666", created_at=mydate_iso, updated_at=mydate_iso)
        myplace = Pl
        self.assertEqual(myplace.id, "666666")
        self.assertEqual(myplace.created_at, mydate)
        self.assertEqual(myplace.updated_at, mydate)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests For Testing Save Method.
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
        myplace = Place()
        sleep(0.05)
        first_updated_at = myplace.updated_at
        myplace.save()
        self.assertLess(first_updated_at, myplace.updated_at)

    def test_two_saves(self):
        myplace = Place()
        sleep(0.05)
        first_updated_at = myplace.updated_at
        myplace.save()
        second_updated_at = myplace.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        myplace.save()
        self.assertLess(second_updated_at, myplace.updated_at)

    def test_save_with_arg(self):
        myplace = Place()
        with self.assertRaises(TypeError):
            myplace.save(None)

    def test_save_updates_file(self):
        myplace = Place()
        myplace.save()
        myplace_id = "Place." + myplace.id
        with open("file.json", "r") as f:
            self.assertIn(myplace_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests For Testing to_dict Method.
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
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        myplace = Place()
        self.assertIn("id", myplace.to_dict())
        self.assertIn("created_at", myplace.to_dict())
        self.assertIn("updated_at", myplace.to_dict())
        self.assertIn("__class__", myplace.to_dict())

    def test_to_dict_contains_added_attributes(self):
        myplace = Place()
        myplace.middle_name = "Johnson"
        myplace.my_number = 777
        self.assertEqual("Johnson", myplace.middle_name)
        self.assertIn("my_number", myplace.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        myplace = Place()
        myplace_dict = myplace.to_dict()
        self.assertEqual(str, type(myplace_dict["id"]))
        self.assertEqual(str, type(myplace_dict["created_at"]))
        self.assertEqual(str, type(myplace_dict["updated_at"]))

    def test_to_dict_output(self):
        mydate = datetime.today()
        myplace = Place()
        myplace.id = "666666"
        myplace.created_at = myplace.updated_at = mydate
        to_dict = {
            'id': '666666',
            '__class__': 'Place',
            'created_at': mydate.isoformat(),
            'updated_at': mydate.isoformat(),
        }
        self.assertDictEqual(myplace.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        myplace = Place()
        self.assertNotEqual(myplace.to_dict(), myplace.__dict__)

    def test_to_dict_with_arg(self):
        myplace = Place()
        with self.assertRaises(TypeError):
            myplace.to_dict(None)


if __name__ == "__main__":
    unittest.main()
