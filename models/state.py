#!/usr/bin/python3
"""
Module: state.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ the state class that inherits from BaseModel
    and stores the information of User's State """
    name = ''

    def __init__(self, state='', *args, **kwargs):
        """ initializes the state class """
        super().__init__(*args, **kwargs)
        self.state = str(state)
