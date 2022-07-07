#!/usr/bin/python3

'''
filter(func,iterable)
This function returns iterable same as map
'''

li = [("a",2),("b",11),("m",9),("g",1)]

x = list(filter(lambda iter:iter[1]>5,li)) # This one will have a list of tuples
x = list(map(lambda iter:iter[1]>5,li)) #This one will have a list of true false 
print(x)