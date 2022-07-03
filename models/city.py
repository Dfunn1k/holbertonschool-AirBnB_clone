#!/usr/bin/python3
"""City Class implementation"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class that inherits from Basemodel

    Attributes:
        state_id (str): The state id.
        name (str): The name of the state.
    """

    state_id = ""
    name = ""
