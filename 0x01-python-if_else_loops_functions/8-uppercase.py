#!/usr/bin/python3
def uppercase(str):
    answer = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            answer += chr(ord(i) - 32)
        else:
            answer += i
            print("{}".format(answer))
