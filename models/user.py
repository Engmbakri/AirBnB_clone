#!/usr/bin/python3
"""
User class Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
