#!/usr/bin/python
""" Class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ User creation class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize """

        super().__init__(*args, **kwargs)
