#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    m = len(sys.argv) - 1
    if m == 1:
        print("{:d} argument:".format(m))
    elif m == 0:
        print("{:d} arguments.".format(m))
    else:
        print("{:d} arguments:".format(m))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
            i += 1
