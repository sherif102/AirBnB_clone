#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

count = 0
value = "City"

all_objects = storage.all()
obj_lists = list(all_objects.values())
for x in obj_lists:
    if x.__class__.__name__ == value:
        count += 1
    print(x.__class__.__name__)

print(f'The number of {value}:- {count}')