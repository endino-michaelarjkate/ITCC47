class Stack:
    """Singly Linked List implementation of a stack data structure."""

    class Node:
        def __init__(self, item: int, pointer: int):
            self.__item = item 
            self.__pointer = pointer 

        def setPointer(self, newPointer: 'Stack.Node'):
            self.__pointer = newPointer

        def getPointer(self):
            return self.__pointer 
        
        def setItem(self, newItem):
            self.__item = newItem 

        def getItem(self):
            return self.__item 

        def __str__(self):
            return self.__item 
        
    # __capacity = 5

    def __init__(self):
        self.__sentinel = Stack.Node(None, None) #always points to the top element of the stack 
        self.__size = 0

    def incrSize(self):
        self.__size += 1

    def dcrSize(self):
        self.__size -= 1 

    def isEmpty(self):
        return self.__sentinel.getPointer() is None 
    
    def push(self, item: int):
        newNode = Stack.Node(item, None) 
        newNode.setPointer(self.__sentinel.getPointer())
        self.__sentinel.setPointer(newNode)
        self.incrSize() 
        
        
    def pop(self):

        if not self.isEmpty():
            temp = self.__sentinel.getPointer() 
            self.__sentinel.setPointer(temp.getPointer())
            temp.setPointer(None)
            self.dcrSize()
            return temp 
        
    def peek(self):
        if not self.isEmpty():
            return self.__sentinel.getPointer()  
        else:   
            print("Stack is empty")
            return None  
            
    def __str__(self):
        s = ""
        n = self.__sentinel.getPointer()  
        if not self.isEmpty():
            s += f"Top Element is {n.getItem()}"
            s += "\nElements in the stack: "
            while n is not None:
                s += "\n" + str(n.getItem()) 
                n = n.getPointer() 
        else:
            s += "Stack is empty"
        return s 

             



myStack = Stack()  
myStack.push(3)
myStack.push(1)
myStack.push(5)
myStack.pop() 
myStack.push(7)
print(myStack) 
         

    
