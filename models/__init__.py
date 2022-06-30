#!/usr/bin/python3
""""""
from .engine import file_storage
from models.base_model import BaseModel

dict_class = {
    "BaseModel": BaseModel
}

storage = file_storage.FileStorage()
storage.reload()
