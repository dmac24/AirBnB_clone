#!/usr/bin/python3
"""File Storage module"""

import json


class FileStorage():
    """Class File storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all"""
        return self.__objects

    def new(self, obj):
        """new"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """save"""
        to_json = {}
        if self.__objects is None:
            return
        # creando nuevo diccionario
        for key in self.__objects.keys():
            to_json[key] = self.__objects[key].to_dict()
        # guardando / serializando con json
        with open(self.__file_path, "w") as f:
            json.dump(to_json, f)

    def reload(self):
        """ Reloads """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
