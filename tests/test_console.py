import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        base_model = BaseModel()

        self.storage.new(base_model)

        self.assertIn(f"BaseModel.{base_model.id}", self.storage.all())

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_save_red(self):
        base_model = BaseModel()
        user = User()

        self.storage.new(base_model)
        self.storage.new(user)

        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(self.storage.all(), new_storage.all())

        self.assertIn(f"BaseModel.{base_model.id}", new_storage.all())
        self.assertIn(f"User.{user.id}", new_storage.all())


if __name__ == '__main__':
    unittest.main()
