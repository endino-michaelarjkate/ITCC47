class ArrayList:
    def __init__(self, size: int = 50):
        self.__list = [None] * size
        self.__size = 0 

    def getFirst(self):
        return self.__list[0]
    
    def incrSize(self):
        self.__size += 1

    def dcrSize(self):
        self.__size -= 1

    def insert(self, item):
        index = 0 
        while index < self.__size:
            if item < self.__list[index]:
                break 
            index += 1

        start = self.__size 
        while start > index:
            self.__list[start] = self.__list[start-1] 
            start -= 1

        self.__list[index] = item
        self.incrSize() 

    def get(self, index):
        if index < 0 or index >= self.__size:
            return False
        return self.__list[index]
    
    def update(self, item, index):
        if index < 0 or index >= self.__size:
            return False
        self.__list[index] = item 
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.__size:
            return False
        
        deleted = self.get(index)

        while index < self.__size:
            self.__list[index] = self.__list[index+1] 
            index += 1

        self.dcrSize() 
        return deleted
    
    def __str__(self):
        s = "["
        for x in range(self.__size):
            s += str(self.__list[x]) 
            if x != self.__size - 1:
                s += ","
        s += "]"
        return s 




myArray = ArrayList() 
myArray.insert(0)
myArray.insert(10)
myArray.insert(-1)
myArray.insert(6)
myArray.insert(-7)
print(myArray)
myArray.update(100,2)
print(myArray)
myArray.remove(3)
print(myArray)
        




