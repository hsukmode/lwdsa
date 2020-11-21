"""
Implements a dynamic array 
"""
from typing import Any


class DynamicArray:
    def __init__(self, capacity: int):
        """creates a dynamic array

        Args:
            capacity (int): initial capacity of the DynamicArray
        """
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
        
    def _resize(self):
        """resize array"""
        self.capacity = self.size * 2
        resized_array = [None] * self.capacity
        for idx, val in enumerate(self.array):
            resized_array[idx] = val
        self.array = resized_array

    def add(self, val: Any):
        """'append' a value to the DynamicArray

        Args:
            val (Any): value to add to the end of the DynamicArray
        """
        if self.size == self.capacity:
            self._resize()

        self.array[self.size] = val
        self.size += 1

    def pop(self):
        pass


    def get(self, idx: int) -> Any:
        """gets the value of a specified index in DynamicArray

        Args:
            idx (int): index of the DynamicArray

        Raises:
            IndexError: out of bounds 

        Returns:
            [Any]: value in DynamicArray at idx
        """
        if 0 > idx > self.length:
            raise IndexError("inaccessable index")
        print(self.array)
        return self.array[idx]
