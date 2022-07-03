#!/usr/bin/python3
"""User Class implementation"""
from .base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
