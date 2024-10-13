class ArrayList:

    def __init__(self, size: int = 50):
        self.__list = [0] * size
        self.__size = 0

    def getFirst(self) -> int:
        return self.get(0)

    def get(self, index: int) -> int:
        return self.__list[index]

    def getSize(self) -> int:
        return self.__size

    def incrSize(self):
        self.__size += 1

    def decrSize(self):
        self.__size -= 1

    def insert(self, item: int):
        """
        Inserts a new item at the correct position.
        :param item: Item to be inserted.
        :return: Nothing.
        """

        i = 0
        while i < self.getSize():
            if item < self.get(i):
                break

            i += 1

        # Adjust array list
        j = self.getSize()

        while j > i:
            self.__list[j] = self.__list[j - 1]
            j -= 1

        self.__list[i] = item
        self.incrSize()

    def update(self, item: int, index: int) -> bool:
        """
        Updates the element at index with new value.
        :param item: New value.
        :param index: Index. Starts from 0 to size - 1.
        :return: Flag if update was successful or not.
        """
        if index >= self.getSize():
            return False

        self.__list[index] = item
        return True

    def remove(self, index: int) -> int:
        """
        Removes item at index.
        :param index: Index of item to be removed.
        :return: Value of element at index. -1 if index out of bounds.
        """
        if index >= self.getSize():
            return -1

        res = self.get(index)

        while index < self.getSize():
            self.update(self.get(index + 1), index)
            index += 1

        self.decrSize()

        return res

    def __str__(self) -> str:
        """
        Prints the content of this array list.
        :return:
        """
        s = "[ "

        i = 0
        while i < self.getSize():
            s += str(self.get(i))

            if i + 1 < self.getSize():
                s += ", "

            i += 1

        s += " ]"
        return s

arr = ArrayList()
arr.insert(10)
arr.insert(20)
arr.insert(30)
arr.insert(17)

arr.remove(3)
print(arr)