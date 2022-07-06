#!/usr/bin/python

def even(n):
    li = []
    for i in range(0,n,2):
        li.append(i)
    return li
        
li = even(int(input("Enter the limit upto which you want even numbers: ")))
print(li)