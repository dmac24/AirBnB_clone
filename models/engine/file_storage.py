#!/usr/bin/python3


import json


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
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
        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
