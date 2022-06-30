#!/usr/bin/python3
""""""

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
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """"""
        new_dict = self.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """"""
        if path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as file:
                reader = file.read()
                if len(reader) == 0:
                    return
                models_json = json.loads(reader)
            for model in models_json.values():
                if model['__class__'] == "BaseModel":
                    self.new(BaseModel(**model))
                elif model['__class__'] == "User":
                    self.new(User(**model))
                elif model['__class__'] == "State":
                    self.new(State(**model))
                elif model['__class__'] == "City":
                    self.new(City(**model))
                elif model['__class__'] == "Amenity":
                    self.new(Amenity(**model))
                elif model['__class__'] == "Place":
                    self.new(Place(**model))
                elif model['__class__'] == "Review":
                    self.new(Review(**model))
