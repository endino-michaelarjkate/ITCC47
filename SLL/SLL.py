class SLL:
    class Node:

        def __init__(self, item: int, pointer: 'SLL.Node'):
            self.__item = item
            self.__pointer = pointer

        def getItem(self) -> int:
            return self.__item

        def getPointer(self) -> 'SLL.Node':
            return self.__pointer

        def setItem(self, item: int) -> None:
            self.__item = item

        def setPointer(self, pointer: 'SLL.Node') -> None:
            self.__pointer = pointer

        def __str__(self) -> str:
            """
                :return: String representation of this object, the value of the node.
                """
            return str(self.__item)

    def __init__(self):
        self.__size = 0
        self.__sentinel = SLL.Node(None, None)

    def getSize(self) -> int:
        return self.__size

    def incrSize(self):
        self.__size += 1

    def decrSize(self):
        self.__size -= 1

    def getFirst(self):
        return self.__sentinel.getPointer()

    def insert(self, item: int):
        """
        Inserts a new item at the correct position.
        :param item: Item to be added to the linked list.
        :return: Nothing.
        """

        new_node = SLL.Node(item,None) # creates a new node that is not currently linked to the list 
        prev_node = self.__sentinel 
        n = self.getFirst() # gets the 1st node of the list, returns None if list is empty 

        while n is not None: # if list is not empty 
            if item < n.getItem(): # checks if new node can be inserted before current first node 
                break 
            prev_node = n 
            n = n.getPointer() 

        prev_node.setPointer(new_node)
        new_node.setPointer(n) 

        self.incrSize()     

    def get(self, pos: int) -> 'SLL.Node':
        """
        :param pos: Position of node to retrieve. Starts from 1 to size of the SLL.
        :return: Node if found. None if out of bounds.
        """
        if pos > self.__size or pos <= 0:
            return None 
        
        n = self.getFirst() 
        pos -= 1
        counter = 0 

        while pos > counter:
            n = n.getPointer() 
            counter += 1

        return n 

    def update(self, item: int, pos: int) -> bool:
        """
        Updates item of the node at given position.
        :param item: New value.
        :param pos: Position of the node. Starts from 1 to size of the SLL.
        :return: Flag if update was successful or not.
        """
        n = self.get(pos)

        if n is None:
            return False

        n.setItem(item)

        return True

    def remove(self, pos: int) -> 'SLL.Node':
        """
        Removes node at the position given.
        :param pos: Position of the node. Starts from 1 to size of the SLL.
        :return: Node that was removed.
        """
        if pos > self.__size:
            return None

        prev_node = self.__sentinel
        n = self.getFirst()
        pos -= 1
        counter = 0

        while pos > counter:
            counter += 1
            prev_node = n
            n = n.getPointer()

        prev_node.setPointer(n.getPointer())
        n.setPointer(None)

        return n

    def __str__(self) -> str:
        """
        Prints all items present in this SLL.
        :return:
        """
        s = ""

        if self.__size == 0:
            return "This singly-linked list is empty..."

        n = self.getFirst()

        while n is not None:
            s += str(n)

            if n.getPointer() is not None:
                s += " -> "

            n = n.getPointer()

        return s


sll = SLL()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.insert(17)
# print(sll.get(1))
# print(sll.get(2))
# print(sll.get(3))
# print(sll.get(4))
# print(sll.get(0))
# print(sll.get(10))
print(sll.remove(4))

print(sll)
