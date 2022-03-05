#!/usr/bin/python
""" Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ R eview """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ initialize """
        super().__init__(*args, **kwargs)
