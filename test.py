#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

dic = {"name": "sheriff", "age": 24, "school": "UNILORIN"}

all_objects = storage.all()
obj_lists = list(all_objects.values())
value = obj_lists[0]

x = """update("}38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})"""

# x = 'update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", "89")'
front = x.index('{')
back = x.rindex('}') + 1
print(front)
print(back)
value = x[front:back]
print(value)
print(type(eval(value)))
print(x[9:45])
# print(x)
# print(len(y))
# print()
# print("####")
# for x in y:
#     print(x)
# print(type(dic) == dict)