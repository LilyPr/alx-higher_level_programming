#!/usr/bin/python3
import sys
if __name__ == "__main__":
     """Prints the argument list passed to the program

     The program takes all the arguments starting from the second
     and prints the number of arguments and their value
     """
    m = len(sys.argv) - 1
    if m == 0:
        print("0 arguments.")
    elif m == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(m))
    for i in range(m):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
