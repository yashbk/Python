#!/usr/bin/python

#Recursive function to get factorial of a number
def fact(num):
    if num == 0:
        return 1 
    else:
        return num * fact(num-1)

val = fact(int(input("Enter a number to get it's factorial: ")))
print(f"Factorial of a entered number is {val}")