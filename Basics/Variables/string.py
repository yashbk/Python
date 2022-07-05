#!/usr/bin/python

'''
syntax:
variable_name = 'value'
variable_name = "value"
'''

#string
x="thundersoft"
print(x) #display x
print(type(x))#display the data type of x:

#Operations on strings
#String slicing

str1 = x[:]
print(str1)
str2 = x[:3]
print(str2)
str3 = x[3:]
print(str3)
str4 = x[1:4]
print(str4)
str5 = x[0:-1:2] #Take every second character
print(str5)

#string concatenation
str1 = "hello"
str2 = "welcome"
str3 = str1 +" "+ str2
print(str3)

#membership operator
if "h" in "hello":
    print(True)
else:
    print(False)
    
#identity operator
print(str1 is not str2)

#Type conversion
li = list(x)
print("li is ",type(li))

one = 5
n = str(one)
print("n is ",type(n))
two = int(n)
print(two)