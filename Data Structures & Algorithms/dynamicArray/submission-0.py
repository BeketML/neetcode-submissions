class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("capacity must be > 0")

        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity


    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("I is incorrect")
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("I is incorrect")
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        
        self.array[self.size] = n
        self.size+=1
        
    def popback(self) -> int:
        if self.size == 0:
            raise ValueError("Cannot pop empty array")

        value = self.array[self.size-1]
        self.size -= 1
        return value
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array


    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
