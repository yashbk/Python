#!/usr/bin/python

def bubble(arr):
    for i in range(len(arr)):
        for j in range (len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                

arr = [7,6,5,8,2,0,1,4,6,2]
print("Before sorting ",arr)
bubble(arr)
print("After sorting ",arr)