#!/usr/bin/python3
"""Module 5-to_json_string,returns the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
