#!/usr/bin/python3

li1 = [1,3,4,5,6,8]
li2 = li1
print("id of li1: ",id(li1))
print("id of li2: ",id(li2))

li3 = li1.copy()
print("id of li3: ",id(li3))

#In shallow copy if we change list elements then it will affect the other list
#In deep copy it won't affect.
li1[2] = 20
print("li1: ",li1)
print("li2: ",li2)
print("li3: ",li3)