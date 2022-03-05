#!/usr/bin/python
""" Class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity """
    def __init__(self, *args, **kwargs):
        """ initialize """
        if len(kwargs) == 0:
            self.name = ""
        super().__init__(*args, **kwargs)
