#!/usr/bin/python3
def max_integer(my_list =[]):
    if not my_list:
        return None

    mx = min(my_list)
    for n in my_list:
        if n > mx:
            mx = n
    return mx 
