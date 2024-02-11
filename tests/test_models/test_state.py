#!/usr/bin/python3
"""
State Unittest Module
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """
    Unittests For testing Instantiation Of The State Class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_is_public_class_attribute(self):
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_states_different_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_states_different_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        mydate = datetime.today()
        mydate_repr = repr(mydate)
        state = State()
        state.id = "666666"
        state.created_at = state.updated_at = mydate
        state_str = state.__str__()
        self.assertIn("[State] (666666)", state_str)
        self.assertIn("'id': '666666'", state_str)
        self.assertIn("'created_at': " + mydate_repr, state_str)
        self.assertIn("'updated_at': " + mydate_repr, state_str)


    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        state = State(id="345", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, my_date)
        self.assertEqual(state.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
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
        the_state = State()
        sleep(0.05)
        firstupdatedat = the_state.updated_at
        the_state.save()
        self.assertLess(firstupdatedat, the_state.updated_at)

    def test_two_saves(self):
        the_state = State()
        sleep(0.05)
        firstupdatedat = the_state.updated_at
        the_state.save()
        secondupdatedat = the_state.updated_at
        self.assertLess(firstupdatedat, secondupdatedat)
        sleep(0.05)
        the_state.save()
        self.assertLess(secondupdatedat, the_state.updated_at)

    def test_save_with_arg(self):
        the_state = State()
        with self.assertRaises(TypeError):
            the_state.save(None)

    def test_save_updates_file(self):
        the_state = State()
        the_state.save()
        the_stateid = "State." + the_state.id
        with open("file.json", "r") as f:
            self.assertIn(the_stateid, f.read())


class TestState_to_dict(unittest.TestCase):
    """
    Unittests For Testing to_dict Method.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        the_state = State()
        self.assertIn("id", the_state.to_dict())
        self.assertIn("created_at", the_state.to_dict())
        self.assertIn("updated_at", the_state.to_dict())
        self.assertIn("__class__", the_state.to_dict())

    def test_to_dict_contains_added_attributes(self):
        the_state = State()
        the_state.middle_name = "Khartoum"
        the_state.my_number = 777
        self.assertEqual("Khartoum", the_state.middle_name)
        self.assertIn("my_number", the_state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        the_state = State()
        the_state_dict = the_state.to_dict()
        self.assertEqual(str, type(the_state_dict["id"]))
        self.assertEqual(str, type(the_state_dict["created_at"]))
        self.assertEqual(str, type(the_state_dict["updated_at"]))

    def test_to_dict_output(self):
        mydate = datetime.today()
        the_state = State()
        the_state.id = "666666"
        the_state.created_at = the_state.updated_at = mydate
        tdict = {
            'id': '666666',
            '__class__': 'State',
            'created_at': mydate.isoformat(),
            'updated_at': mydate.isoformat(),
        }
        self.assertDictEqual(the_state.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        the_state = State()
        self.assertNotEqual(the_state.to_dict(), the_state.__dict__)

    def test_to_dict_with_arg(self):
        the_state = State()
        with self.assertRaises(TypeError):
            the_state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
