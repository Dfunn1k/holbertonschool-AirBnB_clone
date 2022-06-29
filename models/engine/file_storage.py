#!/usr/bin/python3
import json


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
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.loads(f.read())
                for key, value in self.__objects.items():
                    pass#falta implementar
        except FileNotFoundError:
            pass
