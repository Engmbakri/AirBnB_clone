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
        # Create an instance of BaseModel
        base_model = BaseModel()

        # Add the instance to the storage
        self.storage.new(base_model)

        # Check if the instance is in the storage
        self.assertIn(f"BaseModel.{base_model.id}", self.storage.all())

    def test_all(self):
        # Check if all method returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)

    def test_save_reload(self):
        # Create instances of BaseModel and User
        base_model = BaseModel()
        user = User()

        # Add instances to the storage
        self.storage.new(base_model)
        self.storage.new(user)

        # Save the data to the file
        self.storage.save()

        # Reload the data from the file
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded storage has the same data
        self.assertEqual(self.storage.all(), new_storage.all())

        # Check if the reloaded storage has the instances
        self.assertIn(f"BaseModel.{base_model.id}", new_storage.all())
        self.assertIn(f"User.{user.id}", new_storage.all())


if __name__ == '__main__':
    unittest.main()
