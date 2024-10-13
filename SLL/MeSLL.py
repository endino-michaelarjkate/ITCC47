class SLL:
    class Node:
        def __init__(self, item: int, pointer: 'SLL.Node'):
            self.__item = item 
            self.__pointer = pointer 

        def getItem(self):
            return self.__item 
        
        def getPointer(self):
            return self.__pointer
        
        def setItem(self, item: int):
            self.__item = item 

        def setPointer(self, pointer: 'SLL.Node'):
            self.__pointer = pointer
        
        def __str__(self):
            return str((self.__item))
        
    def __init__(self):
        self.__size = 0
        self.__sentinel = SLL.Node(None,None)

    def getFirst(self):
        return self.__sentinel.getPointer()
    
    def getLast(self):
        return self.get(self.__size) 
    
    def getSentinel(self):
        return self.__sentinel 
        
    def incrSize(self):
        self.__size += 1

    def dcrSize(self):
        self.__size -= 1

    def getSize(self):
        return self.__size

    # def insert(self, item: int):
        # new_node = SLL.Node(item,None)

        # prev_node = self.__sentinel 
        # n = self.getFirst() 

        # while n is not None:
        #     if item < n.getItem():
        #         break 
        #     prev_node = n
        #     n = n.getPointer() 

        # prev_node.setPointer(new_node)
        # new_node.setPointer(n)

        # self.incrSize() 

    def insert(self, item):
        new_node = SLL.Node(item, None)

        prev_node = self.__sentinel
        n = prev_node.getPointer() 

        while n is not None:
            if item < n.getItem():
                break 
            prev_node = n
            n = n.getPointer() 


        prev_node.setPointer(new_node)
        new_node.setPointer(n) 

        self.incrSize() 

    # def get(self, pos: int):
    #     """
    #     Parameter: pos (int) - position of node item to get
    #     """
    #     if pos > self.__size or pos <= 0:
    #         return None 
        
    #     n = self.getFirst()
    #     pos -= 1
    #     counter = 0 

    #     while pos > counter:
    #         n = n.getPointer()
    #         counter += 1

    #     return n 
    
    def get(self, pos):
        if pos > self.__size and pos <= 0:
            return None
        counter = 0 
        pos -= 1
        
        n = self.getFirst() 

        while pos > counter:
            n = n.getPointer() 
            counter += 1

        return n 

    def update(self, item, pos):
        if pos > self.__size and pos <= 0:
            return False
        
        pos -= 1
        counter = 0
        n = self.getFirst() 

        while pos > counter:
            n = n.getPointer() 
            counter += 1 

        n.setItem(item) 
        return True 

    # def update(self, item: int, pos: int):
        
    #     n = self.get(pos) 
    #     if n is None:
    #         return "Node does not exist at position."
    #     n.setItem(item) 

    def remove(self, pos):
        deleted = self.get(pos) 
        
        pos -= 1
        counter = 0 

        prev = self.__sentinel 
        n = prev.getPointer()

        while pos > counter:
            prev = n
            n = n.getPointer() 
            counter += 1 

        prev.setPointer(n.getPointer())
        n.setPointer(None) 

        self.dcrSize() 
        return deleted 


    # def remove(self, pos: int):
    #     if pos > self.__size or pos <= 0:
    #         return False
         
    #     prev_node = self.__sentinel
    #     n = self.getFirst() 
    #     pos -= 1 
    #     counter = 0

    #     while pos > counter:
    #         prev_node = n
    #         n = n.getPointer()
    #         counter += 1
        
    #     prev_node.setPointer(n.getPointer())
    #     n.setPointer(None)

    #     self.dcrSize()
    #     return True 

    def __str__(self):
        s = ""
        n = self.getFirst() 

        while n is not None:
            s += n.__str__() 

            if n.getPointer() != None:
                s += " -> "

            n = n.getPointer()

        return s

# def reverseSLL(sll: 'SLL.Node'):
#     prev = None
#     curr = sll.getFirst() 

#     while curr is not None:
#         next = curr.getPointer() 
#         curr.setPointer(prev)
#         prev = curr
#         curr = next 

#     sll.getSentinel().setPointer(prev)

#     return sll 


# def reverseSLL(sll: 'SLL'):
#     prev = None 
#     curr = sll.getFirst() 

#     while curr is not None:
#         next = curr.getPointer() 
#         curr.setPointer(prev) 
#         prev = curr
#         curr = next 

#     sll.getSentinel().setPointer(prev) 
    
#     return sll

def bubbleSort(sll: 'SLL'):

    i = 0
    while i < sll.getSize():
        prev = sll.getSentinel()
        current = sll.getFirst() 
        next = current.getPointer()

        while next is not None:
            if current.getItem() > next.getItem():
                current.setPointer(next.getPointer()) 
                next.setPointer(current) 
                prev.setPointer(next)
                prev = next 
                next = current.getPointer() 
            else: 
                prev = current 
                current = next 
                next = current.getPointer() 

        i += 1


sll = SLL()

sll.insert(30)
sll.insert(10)
sll.insert(20)
sll.insert(17)


# print(sll)
# print(sll.update(1,3))
# print(sll)
# sll.remove(3)
print(sll)
bubbleSort(sll)
print(sll) 
# print(reverseSLL(sll))
