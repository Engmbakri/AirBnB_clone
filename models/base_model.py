#!/usr/bin/python3
"""
module for the BaseModel class.
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    The base model for other classes in the application. It includes methods
    for initializing, saving, converting to a dictionary,
    and providing a string representation.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                else:
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value,
                                '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        models.storage.new(self)

    def save(self):
        """
         Updates the updated_at attribute to the current datetime
         and saves the instance using the storage system.
         """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary for serialization.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['id'] = self.id
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}], ({self.id}), {self.__dict__}"
