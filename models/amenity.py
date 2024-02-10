#!/usr/bin/python3
"""
Module For The Amenity Class Inherited From BseModel .
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent an amenity.

    Attributes:
        name (str): Name Of The Amenity.
    """

    name = ""
