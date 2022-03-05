#!/usr/bin/python
""" Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ City """
    def __init__(self, *args, **kwargs):
        """ initialize """
        if len(kwargs) == 0:
            self.name = ""
            self.state_id = ""
        super().__init__(*args, **kwargs)
