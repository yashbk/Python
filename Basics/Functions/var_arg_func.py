#!/usr/bin/python

def multiple(*tup):  #collects arguments in the form of tuple
    total = 1
    for i in tup:
        total *=i
    return total

print(multiple(1,2,3,4,45,5,6,7))