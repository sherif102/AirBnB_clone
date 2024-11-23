#!/usr/bin/python3
"""
Module: user.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ the user class that inherits from BaseModel
    and stores the information of users """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, email='', password='', first_name='',
                 last_name='', *args, **kwargs):
        """ initializes the user attributes """
        super().__init__(*args, **kwargs)
        self.email = str(email)
        self.password = str(password)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
