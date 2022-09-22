#!/usr/bin/python3
import sys

if __name__ == "__main__":
     """Print the number of and list of arguments."""

    m = len(sys.argv) - 1
    if m == 1:
        print("{:d} argument:".format(m))
    elif m == 2:
        print("{:d} arguments.".format(m))
    else:
        print("{:d} arguments:".format(m))
    for i in range(m):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
