#!/usr/bin/python3
"""Module 1-number_of_lines,counts the  number of lines in a file"""


def number_of_lines(filename=""):
    """Counts lines in filename"""
    with open(filename, 'r' encoding='utf8') as a_file:
        count = 0
        for line in a_file:
            count += 1
        return count
