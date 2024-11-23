#!/usr/bin/python3
"""
Module: amenity.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ the amenity class that inherits from BaseModel
    and stores the information of amenity """
    name = ''

    def __init__(self, name='', *args, **kwargs):
        """ initializes the amenity class """
        super().__init__(*args, **kwargs)
        self.name = str(name)
