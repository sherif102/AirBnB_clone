#!/usr/bin/python3
"""
Module: base_model.py
Author: Sheriff Abdulfatai
"""

import uuid
from datetime import datetime


class BaseModel:
    """ the parent class that monitors every other class of
    the project and in which other classes inherited from """

    def __init__(self):
        """ initializes the BaseMOdel """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ prints the string representation of the class BaseModel """
        return f'[BaseModel] ({self.id}) {self.__dict__}'

    def save(self):
        """ update the instance attribute 'updated_at' with
        the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ it generates the dictionary of all the keys/values
        of __dict__ of the instance """
        dico = {"__class__": "BaseModel"}
        for x in self.__dict__:
            if x[0] == '_':
                continue
            if x == "created_at":
                dico[f'{x}'] = str(self.created_at.isoformat())
                continue
            elif x == "updated_at":
                dico[f'{x}'] = str(self.updated_at.isoformat())
                continue
            dico[f'{x}'] = self.__dict__[x]
        return dico
