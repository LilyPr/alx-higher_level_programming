#!/usr/bin/python3
"""Module 4-append_write, appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """append text to a file"""
    with open(filename, 'a', encoding='utf8') as a_file:
        return a_file.write(text)
