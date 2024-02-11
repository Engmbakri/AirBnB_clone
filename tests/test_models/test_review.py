#!/usr/bin/python3
"""
Testing Review Module
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unittests For Testing Instantiation.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_is_public_class_attribute(self):
        review = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", review.__dict__)

    def test_two_reviews_unique_ids(self):
        review_one = Review()
        review_two = Review()
        self.assertNotEqual(review_one.id, review_two.id)

    def test_two_reviews_different_created_at(self):
        review_one = Review()
        sleep(0.05)
        review_two = Review()
        self.assertLess(review_one.created_at, review_two.created_at)

    def test_two_reviews_different_updated_at(self):
        review_one = Review()
        sleep(0.05)
        review_two = Review()
        self.assertLess(review_one.updated_at, review_two.updated_at)

    def test_str_representation(self):
        mydate = datetime.today()
        mydate_repr = repr(mydate)
        review = Review()
        review.id = "666666"
        review.created_at = review.updated_at = mydate
        review_str = review.__str__()
        self.assertIn("[Review] (666666)", review_str)
        self.assertIn("'id': '666666'", review_str)
        self.assertIn("'created_at': " + mydate_repr, review_str)
        self.assertIn("'updated_at': " + mydate_repr, review_str)

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_instantiation_with_kwargs(self):
        mydate = datetime.today()
        mydate_iso = mydate.isoformat()
        Re = Review(id="666666", created_at=mydate_iso, updated_at=mydate_iso) 
        review = Re
        self.assertEqual(review.id, "666666")
        self.assertEqual(review.created_at, mydate)
        self.assertEqual(review.updated_at, mydate)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """
    Unittests For Testing Save Method.
    """

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
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_two_saves(self):
        review = Review()
        sleep(0.05)
        firstupdated_at = review.updated_at
        review.save()
        secondupdated_at = review.updated_at
        self.assertLess(firstupdated_at, secondupdated_at)
        sleep(0.05)
        review.save()
        self.assertLess(secondupdated_at, review.updated_at)

    def test_save_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        review = Review()
        review.save()
        review_id = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


class TestReview_to_dict(unittest.TestCase):
    """
    Unittests For Testing to_dict Method.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_contains_added_attributes(self):
        review = Review()
        review.middle_name = "Johnson"
        review.my_number = 777
        self.assertEqual("Johnson", review.middle_name)
        self.assertIn("my_number", review.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        mydate = datetime.today()
        review = Review()
        review.id = "666666"
        review.created_at = review.updated_at = mydate
        to_dict = {
            'id': '666666',
            '__class__': 'Review',
            'created_at': mydate.isoformat(),
            'updated_at': mydate.isoformat(),
        }
        self.assertDictEqual(review.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        review = Review()
        self.assertNotEqual(review.to_dict(), review.__dict__)

    def test_to_dict_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
