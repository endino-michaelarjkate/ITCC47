class Stack:
    """Array List implementation of a stack data structure."""

    __capacity = 20 

    def __init__(self):
        self.__stack = [None] * Stack.__capacity 
        self.__size = 0 
        self.__top = -1 

    def getTop(self):
        if self.isEmpty():
            return None
        return self.__stack[self.__top] 
    
    def getSize(self):
        return self.__size 

    def isEmpty(self) -> bool:
        """Checks if stack is empty.
           Returns: True if empty, else False"""
        
        return self.__top < 0  
    
    def isFull(self) -> bool:
        """Checks if stack is full.
           Returns: True if full, else False"""
        
        return self.__top == Stack.__capacity - 1  

    def push(self, item: int):
        """Adds a new element at the top of the stack."""

        if self.isFull():
            print("Stack is full.")
            return None
        self.__top += 1
        self.__stack[self.__top] = item
        self.__size += 1
        # print(f"{item} pushed into stack") 

    def pop(self):
        """Removes the top element of the stack""" 
        if self.isEmpty():
            print("Stack is empty.")
            return None 
        item = self.__stack[self.__top]
        self.__stack[self.__top] = None 
        # print(f"{self.getTop()} popped from stack")
        self.__top -= 1
        self.__size -= 1
        return item 
        
        # i dont understand why it's considered as removing, when it doesn't remove it from the array. but it does remove it from the "stack" 
        # fixed: replaced self.__top with None 

    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
        return self.__stack[self.__top] 

    def __str__(self): 
        s = ""
        if not self.isEmpty():
            s += f"Top Element is: {self.getTop()}"
            s += "\nElements present in stack: " 
            for i in self.__stack[self.__top::-1]:
                s += "\n" + str(i) 
        else: 
            s += "Stack is empty."
        return s 
            

if __name__ == "__main__":
    myStack = Stack() 
    myStack.push(3)
    myStack.push(1)
    myStack.push(5)
    myStack.pop() 
    myStack.push(7)
    print(myStack) 



