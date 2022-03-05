#!/usr/bin/python
""" Class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ user """
    def __init__(self, *args, **kwargs):
        """ initialize"""
        if len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
        super().__init__(*args, **kwargs)
