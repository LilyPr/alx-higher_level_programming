#!/usr/bin/python3
def best_score(a_dictionary):
    n = 0
    result = ""
    if a_dictionary:
        for key, val in a_dictionary.items():
            if val > n:
                result = key
                n = val
        return result
        return None
