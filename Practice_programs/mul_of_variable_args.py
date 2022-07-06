#!/usr/bin/python

def mul(*tup):
    val = 1
    for i in tup:
        val *= i
    return val

print(mul(2,3,4,5,8,6,4))