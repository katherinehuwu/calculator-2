"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

first_input = None

while first_input != "q":
    user_input = raw_input("Please enter prefix notation math problem: ")
    math_dtl = user_input.split(" ")

    if math_dtl[0] == "q":
        break

    elif math_dtl[0] == "+":
        answer = add(int(math_dtl[1]), int(math_dtl[2]))
        print answer