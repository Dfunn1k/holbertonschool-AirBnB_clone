#!/usr/bin/python3
""""""
from .engine import file_storage
from .base_model import BaseModel
from .user import User
from .state import State
from .city import City
from .amenity import Amenity
from .place import Place
from .review import Review

dict_class = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


storage = file_storage.FileStorage()
storage.reload()
