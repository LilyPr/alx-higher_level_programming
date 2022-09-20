#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ab = ("Last digit of ")
digit = number % 10
if number >= 0:
    digit = number % 10
    if number < 0:
        digit = number % -10
if digit > 5:
    print("{}{} is {} and is greater than 5".format(ab, number, digit))
elif digit == 0:
    print("{}{} is {} and is 0".format(ab, number, digit))
else: 
    print("{}{} is {}".format(ab, number, digit), end=" ")
    print("and is less than 6 and not 0")
