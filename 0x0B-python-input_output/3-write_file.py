#!/usr/bin/python3
"""Module 3-write_file, writes a string in a text file"""


def write_file(filename="", text=""):
    """write text in file"""
    with open(filename, 'w', encoding='utf8') as a_file:
        return a_file.write(text)
