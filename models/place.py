#!/usr/bin/python3
"""
Module For The Place Class Inherited From BaseModel Class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): Id Of The City.
        user_id (str): User Id.
        name (str): The place Name.
        description (str): Description Of Place.
        number_rooms (int): Number of rooms In The Place.
        number_bathrooms (int): Bathrooms Number In The place.
        max_guest (int): Maximum Number Of guests In The place.
        price_by_night (int): The Price ber night In The place.
        latitude (float): Latitude Of The Place.
        longitude (float): The Longitude Of The Place.
        amenity_ids (list): List of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
