#!/usr/bin/python3
"""
Module: place.py
Author: Sheriff Abdulfatai
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ the place class that inherits from BaseModel
    and stores the information of place """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, city_id='', user_id='', name='', description='',
                 number_rooms=0, number_bathrooms=0, max_guest=0,
                 price_by_night=0, latitude=0.0, longitude=0.0,
                 amenity_ids=[], *args, **kwargs):
        """ initializes the place class """
        super().__init__(*args, **kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = str(name)
        self.description = str(description)
        self.number_rooms = int(number_rooms)
        self.number_bathrooms = int(number_bathrooms)
        self.max_guest = int(max_guest)
        self.price_by_night = int(price_by_night)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.amenity_ids = amenity_ids
