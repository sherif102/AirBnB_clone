#!/usr/bin/env python3

# dic = """update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})"""
# d = dic.split('"')
# print(len(d))
# print(d)
# dic2 = """update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})"""
# d2 = dic2.split('"')
# print(d2)
# print(len(d2))
some = {"profession": 'software engineer', 'age': 24, "school": "unilorin", 'course': 'applied geophysics'}
for x, y in some.items():
    print(f'{x} - {y}')