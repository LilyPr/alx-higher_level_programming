#!/usr/bin/python3
import sys
if __name__ == "__main__":
    
    argv = sys.argv
    m = len(argv) - 1
    if m == 1:
        print("1 arguments:")
    elif m == 0:
        print("0 argument.")
    else:
        print("{} arguments:".format(m))
    for i in range(m):
        print("{}: {}".format(i + 1, argv[i + 1]))
