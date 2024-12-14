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

# class Model():
#     """ the class of tests for the BaseModel of the program """
#     def setUp(self):
#         """ sets up some variables to be used during test"""
#         self.model = BaseModel()
#         try:
#             os.remove('test_file.json')
#             f1 = FileStorage
#             f1.reload()
#         except:
#             pass
#     def tearDown(self):

f1 = FileStorage
f1.reload
x = f1.all

print(x)