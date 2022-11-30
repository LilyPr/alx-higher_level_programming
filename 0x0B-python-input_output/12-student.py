#!/usr/bin/python3
"""Module 11-student.py, function for Creation of a Student class"""


class Student:
    """Class that represent a student with publc attributes"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """show a dict rep of a Student with specific attribute"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for d in attrs:
            try:
                dictionary[d] = self.__dict__[d]
            else:
                pass
            return dictionary
