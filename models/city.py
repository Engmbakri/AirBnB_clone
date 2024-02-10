#!/usr/bin/python3
"""
City Class Module.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class Inherited From BaseModel Represent a City.

    Attributes:
        state_id (str): Id Of The state.
        name (str): The City's Name.
    """

    state_id = ""
    name = ""
