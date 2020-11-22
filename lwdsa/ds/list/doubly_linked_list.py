"""Implementation of Doubly Linked List"""

from typing import Any, Optional

class DLLNode:

    def __init__(self, val: Any = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.sentinel = DLLNode()
        self.size = 0

    def add_first(self, val: Any):
        """function to add a value to a beginning of DLL
        adds in O(1) time

        Args:
            val (Any): value to add
        """
        cur_first = self.sentinel.next 
        node_to_insert = DLLNode(val = val, next = cur_first)
        self.sentinel.next = node_to_insert

        if self.is_empty():
            self.sentinel.prev = node_to_insert
        self.size += 1

    def add_last(self, val: Any):
        """function to add a value to a beginning of DLL
        adds in O(1) time

        Args:
            val (Any): value to add
        """
        cur_last = self.sentinel.prev 
        node_to_insert = DLLNode(val = val, prev=cur_last)
        self.sentinel.prev = node_to_insert
        cur_last.next = self.sentinel.prev

        if self.is_empty():
            self.sentinel.next = node_to_insert
        self.size += 1

    def remove_first(self) -> None:
        if self.is_empty():
            raise Exception("Nothing to Remove")
        
        new_first = self.sentinel.next.next
        self.sentinel.prev = new_first

    def remove_last(self) -> None:
        pass 

    def remove(self) -> Any:
        pass


    def add(self, val: Any, index: int):
        if index < 0 or index > self.size - 1:
            raise Exception("Invalid Index")
        
        if index == 0:
            self.add_first(val)
        elif index == self.size - 1:
            self.add_last(val)
        else:

            pass

    def get(self, index) -> Index:
        first = self.sentinel.next
        count = 0
        while first:
            first = first.next 
        return first.val        

    def is_empty(self) -> bool:
        return self.size == 0
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        str_representation = []
        first = self.sentinel.next
        while first:
            str_representation.append(f"{first.val}")
            if first.next:
                str_representation.append(" -> ")
            first = first.next
        return ''.join(str_representation)


    