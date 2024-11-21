#!/usr/bin/python3
"""
Module: file_storage.py
Author: Sheriff Abdulfatai
"""

import json

class FileStorage:
    """ serializes and deserializes JSON file """
    def __init__(self):
        """ initializes the filestorage instance """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ returns the dictionary '__objects' """
        return self.__objects

    def new(self, obj):
        """ sets in '__objects' the obj with key/value """
        obj_dict = obj.to_dict()
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj_dict['id']}"] = obj_dict

    def save(self):
        """ serializes '__objects' to JSON file in path: __file_path """
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """ deserializes the JSON file to '__objects' if JSON __file_path exists
        if the file doesn't exist, do nothing and no exception should be raised """
        try:
            with open(self.__file_path, 'r') as file:
                obj = json.load(file)
                self.__objects.update(obj)
        except FileNotFoundError:
            pass
