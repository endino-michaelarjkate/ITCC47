class Stack:
    """Singly Linked List implementation of a stack data structure."""

    class Node:
        def __init__(self, item: int):
            self.__item = item 
            self.__pointer = None 

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
        self.__top = Stack.Node(None) #acts as the "top" element of the stack 

    def isEmpty(self):
        return self.__top.getItem() is None 
    
    def push(self, item: int):
        newNode = Stack.Node(item) 
        newNode.setPointer(self.__top) if not self.isEmpty() else newNode.setPointer(self.__top.getItem())
        self.__top = newNode  

        # problem: the bottom item links to an empty Node, not None. fixed using line 34, but need to improve implementation 
        # where it won't need a conditional maybe 
        
    def pop(self):
        if not self.isEmpty():
            item = self.__top
            temp = self.__top.getPointer() 
            self.__top.setPointer(None)
            self.__top = temp 
            return item 
        else: 
            print("Stack is empty")
            return False 
        
    def peek(self):
        if not self.isEmpty():
            return self.__top 
        else:   
            print("Stack is empty")
            return False 
            
    def __str__(self):
        s = ""
        n = self.__top 
        if not self.isEmpty():
            s += f"Top Element is {self.__top.getItem()}"
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
         

    
