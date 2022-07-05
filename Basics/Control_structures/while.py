#!/usr/bin/python

'''
syntax:
while condition:
    statement
    statement

'''

#Example

num = 5
while num>0:
    print(num)
    num -=1

#printing pattern
row=0
col = 0 
while row<5:
    while col<=row:
        print('*',end=' ')
        col +=1
    row +=1
    col = 0
    print()
        