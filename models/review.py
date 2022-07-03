#!/usr/bin/python3
"""Review Class implementation"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class that inherits from Basemodel

    Attributes:
        place_id (str): The place id.
        user_id (str): The user id.
        text (str): Text review of the place.
    """

    place_id = ""
    user_id = ""
    text = ""
