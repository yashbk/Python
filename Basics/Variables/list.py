#!/usr/bin/python

'''
syntax:
variable_name = [value1,value2,value3,value4,....]

Note : Lists are mutable
1) If a value of a variable can be changed then it is called mutable provided it's id remains same 
even after value change
'''

x=["hello","hi",1,2,[5,4,3]]
print(x)

#mutable
li = [1,2,3,4]
print(li)
print(id(li))
li[1] = 20
print(li)
print(id(li))

print("Length of list is ",len(li))

#Operations on list

one = [1,2,3,4]
two = [5,6,7,8]
three = one+two
print(three)

#Membership operator
if 1 in one:
    print("1 is present")
else:
    print("Not present")

if 9 not in two:
    print("9 not present")

#Type conversion
tup = tuple(one)
print(tup)


