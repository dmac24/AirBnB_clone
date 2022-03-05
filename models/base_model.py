#!/usr/bin/python3
""" BaseModel Class """

from datetime import datetime
import uuid


class BaseModel:
    """Define attributes class from future classes will be derived"""
time = "%Y-%m-%dT%H:%M:%S.%f"
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            self.__dict__ = kwargs
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                           self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
