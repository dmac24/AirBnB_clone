#!/usr/bin/python3
""" BaseModel Class """

import uuid
from datetime import datetime
import models

class BaseModel:
    """Define attributes class from future classes will be derived"""


    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if args is not None:
            pass
        if kwargs and len(kwargs) != 0:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Representation of the BaseModel class"""
        return "[{s.__class__.__name__}] ({s.id}) {s.__dict__}".format(s=self)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        return new_dict
