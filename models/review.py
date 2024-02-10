#!/usr/bin/python3
"""
Review Class Module.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): Id Of The Place.
        user_id (str): User Id.
        text (str): Text for the review.
    """

    place_id = ""
    user_id = ""
    text = ""
