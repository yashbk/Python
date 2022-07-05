#!/usr/bin/python

def func(a,b):
    print("The value is ",a);
    for i in range(0,a,2):
        print(i)
    for i in range(0,b):
        print(i)

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
func(num1,num2)