#!/usr/bin/python3
"""Module 8-load_from_json_file,creates an object from a "JSON file."
"""


import json


def load_from_json_file(filename):
    """Creates an obj from filename"""
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
