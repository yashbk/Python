#!/usr/bin/python3

#Sorting datatypes using sorted() function
#sorted function returns a list so you can pass any iterable data type and get a list

#list
li = [5,7,2,9,1,0]
print("Before sorting: list = ", li)
li = sorted(li)
print("After sorting: list = ", li)

li = [5,7,2,9,1,0]
print("Before sorting: list = ", li)
li = sorted(li,reverse = True)
print("After sorting: list = ", li)

#tuple
tup = (5,4,7,9,2,4,2)
print("Before sorting: tup = ", li)
tup = sorted(tup)
print("After sorting: tup = ", tup)

tup = (5,4,7,9,2,4,2)
print("Before sorting: tup = ", li)
tup = sorted(tup,reverse = True)
print("After sorting: tup = ", tup)

#string

str = "hello world"
print("Before sorting: str = ", str)
str = sorted(str)
print("After sorting: str = ", str)

str = "hello world"
print("Before sorting: str = ", str)
str = sorted(str,reverse = True)
print("After sorting: str = ", str)