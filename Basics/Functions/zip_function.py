#!/usr/bin/python3

'''
syntax:
zip(list/string/tuple,list/string/tuple,....)

'''

list1 = [1,2,3,4,5,6,7]
list2 = "abcdefg"
# We want this [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]

list3 = []
tup = []
for i in range(7):
    tup.append(list1[i])
    tup.append(list2[i])
    list3.append(tuple(tup)) 
    tup.clear()

print(list3)

#This can be achieved easily using zip function
list4 = list(zip(list1,list2))
print(list4)

list5 = list(zip("hell",list1,list2,[1,2])) #min len object determines the len of list5
print(list5)