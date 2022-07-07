#!/usr/bin/python3

'''
syntax:
map(func,*iter)
map function returns iterable like range function so
To get the output we need to iterate over the returned value
'''

#Example

li = [("a",2),("b",11),("m",9),("g",1)]

x = list(map(lambda iter:iter[0],li))
print(x)

#The following is same as the above
x = []
for iter in li:
    x.append(iter[0])
    
#Using list comprehension

x = [item[1] for item in li] # syntax [expression for i in something]
                            #         [expression for i in something if i>5]

