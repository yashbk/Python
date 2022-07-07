#! /usr/bin/python3

'''
syntax : 
lambda parameter:expression
'''

li = [("a",2),("b",11),("m",9),("g",1)]

li.sort(key=lambda item:item[1]) 
print(li)