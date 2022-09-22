#!/usr/bin/python3
import sys
if __name__ == "__main__":
    m = len(sys.argv) - 1
    if m == 1:
        print("1 arguments:")
    elif m == 2:
        print("2 arguments.")
    else:
        print("{} arguments:".format(m))
    for i in range(m):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
