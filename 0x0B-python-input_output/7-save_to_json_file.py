#!/usr/bin/python3
"""Module 7-save_to_json_file,writes an object to a text file by
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an my_obj to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
