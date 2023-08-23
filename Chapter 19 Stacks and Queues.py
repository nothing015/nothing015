# Procedural Code

#stack
stack = [None for index in range(0,10)]
basePointer = 0
topPointer = -1
stackFull = 10
item = None

def pop():
    global topPointer, item
    if topPointer == basePointer -1:
        print("Stack is empty,cannot pop")
    else:
        item = stack[topPointer]
        topPointer = topPointer -1

def push(item):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[topPointer] = item
    else:
        print("Stack is full, cannot push")

#queue
queue = [None for index in range(0,10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0

def enQueue(item):                                    # Add item to queue
    global queueLength, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
        queueLength = queueLength + 1
        queue[rearPointer] = item
    else:
        print("Queue is full, cannot enqueue")

def deQueue():                                             # Remove item from queue 
    global queueLength, frontPointer, item
    if queueLength == 0:
        print("Queue is empty,cannot dequeue")
    else:
        item = queue[frontPointer]
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
    queueLength = queueLength -1         



        
# Object-oriented code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value        
