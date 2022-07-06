#!/usr/bin/python

def str_len(str):
	count = 0
	for i in str:
		count = count + 1
	return count

str = "yashas"
len = str_len(str)
print(len)

