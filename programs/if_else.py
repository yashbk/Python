#!/usr/bin/python

#if else

def call():
    print("Function called")
    
A = 3

if A!=0:
    print("A is not equal to zero")
    if A>0:
        print("A is a positive number")
        if A%2==0:
            print("A is a even number")
        else:
            print("A is a odd number")
    else:
        print("A is a negative number")
elif A == "hello":
    print("A is equal to zero")
else:
    print("Something")

call()
