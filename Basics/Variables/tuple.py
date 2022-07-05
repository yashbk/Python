#!/usr/bin/python

'''
syntax:
variable_name = (value1,value2,value3,value4,....)

Note : Tuples are immutable
1) If a value of a variable cannot be changed then it is called immutable.
'''

x=("hello","hi",1,2,[5,4,3])
print(x)
#once defined, tuple values can't be changed but mutable value inside tuple can be changed
x[4][0] = 9
print(x)

#immutable
tup = (1,2,[3,7,4,2],"hello",4.3)
print("Length of tuple is ",len(tup))

#Operations on list

one = (1,2,3,4)
two = (5,6,7,8)
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
li = list(one)
print(li)
b = tuple(li)
print(b)