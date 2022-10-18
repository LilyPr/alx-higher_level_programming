#!/usr/bin/python3
"""This module defines the say_my_name function
"""


def say_my_name(first_name, last_name=""):
<<<<<<< HEAD
    """ Function that prints My name is <first name> <last name> """
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
        if type(first_name) != str:
            raise TypeError('first_name must be a string')
        elif type(last_name) != str:
            raise TypeError('last_name must be a string')
=======
    """ Function that prints a name.
    Args:
        first_name (str): First name.
        last_name (str): Last name.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
>>>>>>> d0d1e5967773372c27909f5e79d1dadf26ab5ba7
