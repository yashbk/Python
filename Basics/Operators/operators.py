#operators
'''
Types of Operator

1)Arithmetic Operators
+ - * / % ** //

2)Comparison (Relational) Operators
> < >= <= == !=

3)Assignment Operators
= += -= /= **= *= %=

4)Logical Operators
and or not

5)Bitwise Operators
& | ^ >> << ~

6)Membership Operators
in  not in

7)Identity Operators
is  is not
'''
#Arithmetic Operators
print("ARITHMETIC OPERATORS")
#addition
a = 2
b = 4
print(a+b)

#subtraction
x = 5
y = 3
print(x - y)

#multiplication
x = 5
y = 3
print(x * y)

#division
x = 12
y = 3
print(x / y)

#modulus
x = 5
y = 2
print(x % y)

#Exponentiation
x = 2
y = 5
print(x ** y)

#floor division
x = 15
y = 2
print(x // y)


#Comparison operators
print("COMPARISION OPERATORS")
x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x <= y)

#assignment operators
print("ASSIGNMENT OPERATORS")
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

#logical operators
print("LOGICAL OPERATORS")
x = 5
print(x > 3 and x < 10)#and

x = 5
print(x > 3 or x < 4)#or

x = 5
print(not(x > 3 and x < 10))#not

#bitwises operators
print("BITWISE OPERATORS")
print("Bitwise ^")
a = 8
b = 2
c = a ^ b 
print(c)

print("Bitwise &")
a = 0xf0
b = 0x0f
c = a & b
print(c)

print("Bitwise |")
a = 0xf0
b = 0x0f
c = a | b
print(c)

print("Bitwise <<")
a = 8 
b = a << 1  #a * 2**shift
print(b)

print("Bitwise >>")
a = 8
b = a>>1 # a / 2**shift
print(b)

print("Bitwise ~")
a = 0
b = ~a
print(b)

#identity operators
print("IDENTITY OPERATORS")
#is
x = 10
y = 10
z = 20
print(x is z)
print(x is y)

#is not
x = 1
y = 4
z = x
print(x is not z)
print(x is not y)


#membership operators
print("MEMBERSHIP OPERATORS")
x = "god mode"
print("mo" in x)

x = "Trinity"
print("TRi" not in x)