"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = raw_input("Please enter prefix notation math problem: ")
    math_dtl = user_input.split(" ")
    answer = None

    if math_dtl[0] == "q":
        break

    elif math_dtl[0] == "+":
        answer = add(int(math_dtl[1]), int(math_dtl[2]))

    elif math_dtl[0] == "-":
        answer = subtract(int(math_dtl[1]), int(math_dtl[2]))
    
    elif math_dtl[0] == "*":
        answer = multiply(int(math_dtl[1]), int(math_dtl[2]))

    elif math_dtl[0] == "/":
        answer = divide(int(math_dtl[1]), int(math_dtl[2]))    

    elif math_dtl[0] == "square":
        answer = square(int(math_dtl[1]))   

    elif math_dtl[0] == "cube":
        answer = cube(int(math_dtl[1])) 

    elif math_dtl[0] == "pow":
        answer = power(int(math_dtl[1]), int(math_dtl[2]))    
    
    elif math_dtl[0] == "mod":
        answer = mod(int(math_dtl[1]), int(math_dtl[2]))   

    else:
        answer = "I don't understand."

    print answer

