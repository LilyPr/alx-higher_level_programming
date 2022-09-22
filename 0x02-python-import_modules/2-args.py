#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    m = len(sys.argv) - 1
    if m == 0:
        print("{:d} argument:".format(m))
    elif m == 1:
        print("{:d} arguments.".format(m))
    else:
        print("{:d} arguments:".format(m))
    for i in range(m):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
