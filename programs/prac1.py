#!/usr/bin/python

def fun():
    a=int(input("Enter a value:"))
    if a==0:
        print("a is zero")
    elif a>0:
        print("a is positive")
        if a%2==0:
            print("a is an even number")
            a = a+1
            for i in range(0,a):
                print(a)
    else:
        print("a is a negative number")

fun()
