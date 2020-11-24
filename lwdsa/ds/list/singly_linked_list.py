"""
Implementation of a singly linked list class
"""
from typing import Literal, Any

class Node:
    def __init__(self, val: None, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    
        
    def __init__(self):
        self.size = 0
        self.first = None

    def add_first(self, val: Any) -> None:
        if self.size == 0:
            self.first = Node(val)
        else:
            second = self.first
            self.first = Node(val, next=second)
        self.size += 1

    def get_first(self) -> Any:
        if self.size == 0:
            raise Exception("Linked List is Size of 0")
        return self.first.val

    def _traverse_to_back(self, listNode: Node) -> Node:
        if listNode.next is None:
            return listNode
        else:
            return self._traverse_to_back(listNode.next)

    def add_last(self, val: Any) -> None:
        if self.size == 0:
            self.first = Node(val)
        else:
            lastnode =  self._traverse_to_back(self.first)
            lastnode.next = Node(val=val)

    def get_last(self) -> Any:
        if self.size == 0:
            raise Exception("Linked List is Size of 0")

        lastnode = self._traverse_to_back(self.first)
        return lastnode.val


    def __len__(self):
        return self.size

    def __repr__(self) -> str:
        str_representation = []
        first = self.first
        while first:
            str_representation.append(f"{first.val}")
            if first.next:
                str_representation.append(" -> ")
            first = first.next
        return ''.join(str_representation)


        
   

    


