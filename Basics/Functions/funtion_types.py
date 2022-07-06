#!/usr/bin/python

'''

1) Functions without return value
    -> Function without arguments and without return value
    -> Function with arguments and without return value
2) Function without return value
    -> Function without argument and with return value
    -> Function with argument and with return value
'''

# Function without arguments and without return value

def func():  #By default returns None
    pass

func()

# Function with arguments and without return value

def func(a,b):  #Function overloading
    print(a+b)

func(2,3)

# Function without argument and with return value

def func():
    return 20

print(func())

# Function with argument and with return value

def func(a,b):
    return a+b 

print(func(4,5))

#Playing with arguments

#Default parameters

def func(a=5,b=3):  #Note default parameters should be always towards the right of normal parameters
    print(a,b)

func()
func(1)
func(9,4)

#Keyword parameter

def func(a=78,b=9):
    print(a,b)
    
func(b = 20)
func(a=98,b=23)