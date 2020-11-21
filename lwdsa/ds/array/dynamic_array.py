"""
Implements a dynamic array 
"""
from typing import Any


class DynamicArray:
    def __init__(self, capacity: int):
        """[summary]

        Args:
            capacity (int): initial capacity of the  Dynamic
        """
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
        self.cur_capacity = self.capacity

    def _resize(self):
        """resize array"""
        resized_array = [None] * self.size * 2
        for idx, val in enumerate(resized_array):
            resized_array[idx] = val
        self.array = resized_array

    def add(self, val: Any):
        """['append' a value to the DynamicArray

        Args:
            val (Any): value to add to the end of the DynamicArray
        """
        if self.cur_idx == self.cur_capacity:
            self._resize()

        self.array[size] = val
        self.size += 1

    def get(self, idx: int) -> Any:
        """gets the value of a specified index in DynamicArray

        Args:
            idx (int): index of the DynamicArray

        Raises:
            IndexError: out of bounds 

        Returns:
            [Any]: value in DynamicArray at idx
        """
        if 0 > self.idx > self.length:
            raise IndexError("inaccessable index")

        return self.array[idx]
