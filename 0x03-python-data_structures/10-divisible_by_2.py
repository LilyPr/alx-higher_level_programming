#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list[:]
    for n in range(len(new)):
        if new[n] % 2 == 0:
            new[n] = True
        else:
            new[n] = False
    return new
