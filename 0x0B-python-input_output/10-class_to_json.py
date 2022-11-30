#!/usr/bin/python3
"""Module 10-class_to_json.py, returns the dictionary description"""


def class_to_json(obj):
    """Creates a dictionary decription of object"""
    return obj.__dict__
