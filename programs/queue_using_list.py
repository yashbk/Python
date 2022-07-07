#!/usr/bin/python3

queue = [] #Empty queue

def enqueue(data):
    queue.append(data)

def dequeue():
    if len(queue) != 0:
        print("Dequeued data is :",queue.pop(0))
    else:
        print("Queue is empty")
    
def display():
    for index,value in enumerate(queue):
        print(f"Value at {index} is {value}")

while True:
    print("Enter the operation you want to perform on queue",
          "1) enqueue",
          "2) dequeue",
          "3) display",
          "q) quit\n",sep='\n')
    value = input()
    if value == "1":
        data = int(input("Enter the data you want to enqueue: "))
        enqueue(data)
        print("Enqueued data is: ",data)
    elif value == "2":
        dequeue()
    elif value == "3":
        display()
    elif value == "q":
        break
    else:
        print("Entered value is invalid please enter again: ")
        
    