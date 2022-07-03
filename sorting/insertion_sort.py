#!/usr/bin/python

def insertion(arr,len):
    for i in range(len-1):
        j=i
        key = arr[i+1]
        while (key<arr[j] and j>=0):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [5,4,3,2,6,7,78,3,2]
print(arr)
len = len(arr)
insertion(arr,len)
print(arr)