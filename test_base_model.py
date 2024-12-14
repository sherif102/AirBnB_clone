#!/usr/bin/python3
"""
Module: test_base_model.py
Author: Sheriff Abdulfatai
"""

import unittest
import json
import models
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
import os

class TestBaseModel(unittest.TestCase):
    """ the class of tests for the BaseModel of the program """
    def setUp(self):
        """ sets up some variables to be used during test"""
        self.model = BaseModel()
        try:
            if os.path.exists('file.json'):
                os.remove('file.json')
            with open('file.json', 'w') as file:
                json.dump({}, file)
            self.f1 = FileStorage
            self.f1.reload()
        except:
            pass
    # def tearDown(self):
    #     """ destroy the variables used during test """
    #     try:
    #         os.remove('file.json')
    #     except:
    #         pass

    def test_public_attributes(self):
        """ tests for the accuracy of public instance attributes on BaseModel """
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(len(self.model.id), 36)
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str(self):
        """ tests for the str output """
        str_output = "[{}] ({}) {}".format("BaseModel", self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), str_output)

    def test_save(self):
        """ tests the save method """
        m1 = BaseModel()
        d1 = m1.updated_at
        m1.save()
        m2 = self.f1.all
        d2 = m2.values[0].updated_at
        self.assertNotEqual(d1, d2)

        


if __name__ == "__main__":
    unittest.main()