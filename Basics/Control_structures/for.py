#!/usr/bin/python

'''
syntax :
for i in range():
    statement
    
for i in list:
    statement
    
for i in string:
    statement
    
'''

#Examples
str = "hello world"
for i in str:
    print(i,end=' ')
print()
    
for i in range(5):
    print(i,end = ' ')
print()

for i in range(5,20,5): #(start,end,step)
    print(i,end=' ')
print()
print()

arr = [1,2,"hello","hi",5,6,8]
print("This is a list: ",end=' ')
for i in arr:
    print(i,end=' ')
print('\n')

arr = (1,2,3,4,5,"hello",8.4)
print("This is a tuple: ",end=' ')
for i in arr:
    print(i,end=' ')
print('\n')