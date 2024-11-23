#!/usr/bin/python3
"""
Module: review.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """ the review class that inherits from BaseModel
    and stores the information of review """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, text='', *args, **kwargs):
        """ initializes the review class """
        super().__init__(*args, **kwargs)
        self.place_id = str(Place().id)
        self.user_id = str(User().id)
        self.text = str(text)
