#!/usr/bin/python3
"""Module 6-from_json_string,returns an object (Python data structure)"""

import json


def from_json_string(my_str):
    """Returns a obj represent by JSON"""
    return json.loads(my_str)
