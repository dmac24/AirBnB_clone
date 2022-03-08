#!/usr/bin/python
""" Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ City """
    
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
