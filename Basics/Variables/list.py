#!/usr/bin/python3

'''
syntax:
variable_name = [value1,value2,value3,value4,....]

Note : Lists are mutable
1) If a value of a variable can be changed then it is called mutable provided it's id remains same 
even after value change
'''

x=["hello","hi",1,2,[5,4,3]]
print(x)

#mutable
li = [1,2,3,4]
print(li)
print(id(li))
li[1] = 20
print(li)
print(id(li))

print("Length of list is ",len(li))

#Operations on list

one = [1,2,3,4]
two = [5,6,7,8]
three = one+two
print(three)

#Membership operator
if 1 in one:
    print("1 is present")
else:
    print("Not present")

if 9 not in two:
    print("9 not present")

#Type conversion
one = [4,5,6,7,8]
tup = tuple(one)
print(tup)

#Unpacking works on tuple and strings too
#List unpacking  
li = [1,2,3,4]
first,second,third,fourth = li
print(first,second,third,fourth)

#unpacking only required objects
li = [1,2,3,4,5]
first,*others,last = li # *other will be a list of all elements except ones which are unpacked
print(first,others,last)

#Looping over lists

li = ["a",1,5,2,5.6]

for value in li:
    print(value,end=' ')
print()

#To get a index of list element we can use enumerate function
li = ["a","b","c","d"]

for index,element in enumerate(li): #enumerate gives a tuple like (0,"a") for every iteration and we are unpacking it to index and element
    print(index,element)

#Inserting value to list
li = ["a","b","c"]
li.append("d") #adds object to last
li.insert(1,"m") #inserts object to specified index
li.pop() #removes last element
li.pop(2) #removes element at specified index
li.remove("a") #removes the object mentioned
del li[1] #deletes element at that index
del li[0:2] #deletes element of those indexes
li.clear() #clears li so will become empty list


#sorting list
#.sort(key,reverse=False)

li = [5,4,7,3,2,6,7]
li.sort() #This will sort li in ascending order
li.sort(reverse=True) #This will sort li in descending order

#using sorted()
new = sorted(li) #sorts li in ascending order and returns sorted list. It won't modify li
new = sorted(li,reverse=True) #sorts li in descending order and returns sorted list. It won't modify li

#sorting complex types
product = [("product1",25),("product2",50),("product3",5)]

#To sort this we need to write our own function to return a value according to which we want to sort
def sort_list(iter):
    return iter[1]
#We can now use a method or function
print(sorted(li,key=sort_list))
li.sort(key=sort_list)
print(li)

#Same using lambda 

li.sort(key=lambda item:item[1])  #lambda parameter:expression
print(li)




