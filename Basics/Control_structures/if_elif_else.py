#!/usr/bin/python

'''
syntax :
if condition:
    statement
    statement
elif condition:
    statement
    statement
else:
    statement
'''

num = int(input("Enter the value "))
print("You entered {0}".format(num))

if num>0 and num <=20:
    print("You are in low band")
elif num >20 and num <=30:
    print("You are in medium band")
elif num>30:
    print("You are in high band")
else:
    print("You entered an invalid value")