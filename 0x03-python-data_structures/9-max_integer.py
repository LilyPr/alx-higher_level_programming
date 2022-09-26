#!/usr/bin/python3
def max_integer(my_list =[]):
    if my_list == []:
        return None

    biggest = min(my_list)
    for n in my_list:
        if n > biggest:
            biggest = n
    return biggest
