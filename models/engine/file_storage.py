#!/usr/bin/python3
"""
FileStorage class
"""

from models.base_model import BaseModel
import json


class FileStorage:
    """to a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
            for key in json_objects:
                self.__objects[key] = BaseModel(**json_objects[key])

        except FileNotFoundError:
            pass
