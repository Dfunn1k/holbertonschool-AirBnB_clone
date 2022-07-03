#!/usr/bin/python3
"""FileStorage Class implementation"""

from os import path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                reader = file.read()
                if len(reader) == 0:
                    return
                models_json = json.loads(reader)
            for model in models_json.values():
                cls_name = model["__class__"]
                self.new(eval(cls_name)(**model))
        except FileNotFoundError:
            return