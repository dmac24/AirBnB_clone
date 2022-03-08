#!/usr/bin/python
""" Class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
