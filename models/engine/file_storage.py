#!/usr/bin/python3
""""""

from os import path
import json
from models.base_model import BaseModel
from models.user import User


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
                self.__objects = json.loads(reader)
            for key, model in self.__objects.items():
                if model['__class__'] == "BaseModel":
                    self.__objects[key] = BaseModel(**model)
                elif model['__class__'] == "User":
                    self.__objects[key] = User(**model)
