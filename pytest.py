#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")

# for x in all_objs.values():
#     print(x.__class__.__name__)
dico = 'show("3da7034c-ddcb-4be2-b266-0513a23c4896")'
print(dico[:4])