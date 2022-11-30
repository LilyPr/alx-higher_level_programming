#!/usr/bin/python3
"""Module 0-read_file
A function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as a_file:
for line in a_file:
print(line, end="")
