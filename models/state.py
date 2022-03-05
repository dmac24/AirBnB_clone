#!/usr/bin/python
""" Class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State """
    def __init__(self, *args, **kwargs):
        """ initialize """
        if len(kwargs) == 0:
            self.name = ""
        super().__init__(*args, **kwargs)
