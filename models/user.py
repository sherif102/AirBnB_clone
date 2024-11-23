#!/usr/bin/python3
"""
Module: user.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ the user class that also inherits from BaseModel
    and stores the information of users """
    def __init__(self, email='', password='', first_name='',
                 last_name='', *args, **kwargs):
        """ initializes the user attributes """
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
