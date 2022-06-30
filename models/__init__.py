#!/usr/bin/python3
""""""
from .engine import file_storage
from .base_model import BaseModel
from .user import User

dict_class = {
    "BaseModel": BaseModel,
    "User": User
}

storage = file_storage.FileStorage()
storage.reload()
