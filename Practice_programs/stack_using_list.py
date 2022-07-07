#!/usr/bin/python3

stack = [] #Empty list

def push(data):
    stack.append(data)

def pop():
    if len(stack) != 0:
        print("Popped data is :",stack.pop())
    else:
        print("Stack is empty")
    
def peek():
    return stack[-1]

def display():
    for index,value in enumerate(stack):
        print(f"Value at {index} is {value}")

while True:
    print("Enter the operation you want to perform on stack","1) push","2) pop","3) peek","4) display","q) quit\n",sep='\n')
    value = input()
    if value == "1":
        data = int(input("Enter the data you want to push: "))
        push(data)
        print("Pushed data is: ",data)
    elif value == "2":
        pop()
    elif value == "3":
        print(peek())
    elif value == "4":
        display()
    elif value == "q":
        break
    else:
        print("Entered value is invalid please enter again: ")
        
    