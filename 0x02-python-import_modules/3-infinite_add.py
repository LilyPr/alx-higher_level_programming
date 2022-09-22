#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    answer = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(len(argv) - 1):
            answer += int(argv[i + 1])
        print(answer)
