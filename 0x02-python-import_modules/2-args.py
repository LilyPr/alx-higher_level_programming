#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    m = len(sys.argv) - 1
    if m == 0:
        print("0 arguments.")
    elif m == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(m))
    for i in range(m):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
