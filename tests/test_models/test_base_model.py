import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch, MagicMock


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_initialization_from_kwargs(self):
        kwargs = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'test_model'
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at, datetime(2023, 1, 1))
        self.assertEqual(base_model.updated_at, datetime(2023, 1, 1))
        self.assertEqual(base_model.name, 'test_model')

    def test_initialization_without_kwargs(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_string_representation(self):
        expected_str = f"[BaseModel], ({self.base_model.id}), {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)


class TestSaveMethod(unittest.TestCase):
    @patch('models.base_model.datetime')
    @patch('models.storage.save')
    def test_save_method(self, mock_save, mock_datetime):
        fixed_datetime = datetime(2024, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = fixed_datetime

        base_model = BaseModel()

        base_model.save()

        self.assertEqual(base_model.updated_at, fixed_datetime)

        mock_save.assert_called_once()


class TestToDict(unittest.TestCase):
    def test_to_dict(self):
        created_at = datetime(2023, 1, 1)
        updated_at = datetime(2023, 1, 2)
        model = BaseModel(id='123', created_at=created_at, updated_at=updated_at)

        obj_dict = model.to_dict()

        self.assertIsInstance(obj_dict, dict)

        expected_keys = ['id', '__class__', 'created_at', 'updated_at']
        for key in expected_keys:
            self.assertIn(key, obj_dict)

        self.assertEqual(obj_dict['id'], '123')
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], '2023-01-01T00:00:00')
        self.assertEqual(obj_dict['updated_at'], '2023-01-02T00:00:00')


class TestBaseModelStr(unittest.TestCase):
    def test_str_representation(self):
        base_model = BaseModel()

        expected_str = f"[BaseModel], ({base_model.id}), {base_model.__dict__}"

        self.assertEqual(str(base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
