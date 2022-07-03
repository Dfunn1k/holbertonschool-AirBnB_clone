#!/usr/bin/python3
"""Place class implementation"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class that inherits from Basemodel

    Attributes:
        city_id (str): The city id.
        user_id (str): The user id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): Number of rooms of the place.
        number_bathrooms (int): Number of bathrooms of the place.
        max_guest (int): Maximum guests of the place.
        price_by_night (int): Price by night of the place.
        latitude (int): Latitude of the place.
        longitude (int): Longitude of the place.
        amenity_ids (list): Amenity Ids of the place.
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
