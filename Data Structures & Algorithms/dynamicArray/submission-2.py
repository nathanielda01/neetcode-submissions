class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dynamic_array = [None] * capacity

    def get(self, i: int) -> int:
        return self.dynamic_array[i]

    def set(self, i: int, n: int) -> None:
        self.dynamic_array[i] = n

    def pushback(self, n: int) -> None:
        i = len(self.dynamic_array)
        if i == 1:
            if self.dynamic_array[i - 1] is None:
                self.dynamic_array[i - 1] = n
                return
            else:
                self.resize()
                self.set(i, n)
                return

        if self.dynamic_array[i - 1] is not None:
            self.resize()
            self.set(i, n)
            return

        while i != 0:
            if self.dynamic_array[i - 1] is None:
                if i - 1 == 0:
                    self.dynamic_array[i - 1] = n
                    return
                i -= 1
                continue
            
            self.dynamic_array[i] = n
            return

    def popback(self) -> int:
        i = len(self.dynamic_array)

        while i != 0:
            if self.dynamic_array[i - 1] is None:
                i -= 1
                continue
            else:
                popped_value = self.dynamic_array[i - 1]
                self.dynamic_array[i - 1] = None
                return popped_value

    def resize(self) -> None:
        self.dynamic_array.extend([None] * self.capacity)
        self.capacity = len(self.dynamic_array)

    def getSize(self) -> int:
        size = 0
        for i in range(len(self.dynamic_array)):
            if self.dynamic_array[i] is not None:
                size += 1
        return size
        
    
    def getCapacity(self) -> int:
        return self.capacity
