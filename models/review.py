#!/usr/bin/python3
"""
Module: review.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ the review class that inherits from BaseModel
    and stores the information of review """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, place_id='', user_id='', text='', *args, **kwargs):
        """ initializes the review class """
        super().__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = str(text)
