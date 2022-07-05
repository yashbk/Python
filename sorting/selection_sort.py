#!/usr/bin/python

def selection(arr):
    length = len(arr)
    for i in range(length-1):
        min = i
        for j in range(i+1,length):
            if arr[min] > arr[j]:
                min = j
            if min!=i:
                temp = arr[i]
                arr[i] = arr[min]
                arr[min] = temp
                
arr = [5,4,3,6,8,2,9,1]
selection(arr)
print(arr)