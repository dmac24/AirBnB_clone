#!/usr/bin/python
""" Class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """ initialize """

        super().__init__(*args, **kwargs)
