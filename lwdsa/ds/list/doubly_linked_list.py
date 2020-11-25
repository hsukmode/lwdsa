"""Implementation of Doubly Linked List"""

from typing import Any


class DLLNode:
    def __init__(self, val: Any = None, prev=None, next=None):
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
        node_to_insert = DLLNode(val=val, next=cur_first)
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
        node_to_insert = DLLNode(val=val, prev=cur_last)
        self.sentinel.prev = node_to_insert
        cur_last.next = self.sentinel.prev

        if self.is_empty():
            self.sentinel.next = node_to_insert
        self.size += 1

    def remove_first(self) -> None:
        """removes first element of linked list

        Raises:
            Exception: [description]
        """
        if self.is_empty():
            raise Exception("Nothing to Remove")

        new_first = self.sentinel.next.next
        self.sentinel.next = new_first
        new_first.prev = self.sentinel

    def remove_last(self) -> None:
        """removes last element of linked list

        Raises:
            Exception: [description]
        """
        if self.is_empty():
            raise Exception("Nothing to Remove")

        second_to_last = self.sentinel.prev.prev
        self.sentinel.prev = second_to_last
        second_to_last.next = None

    def get(self, index: int) -> Any:
        """get value at specified index

        Args:
            index (int): index of value to be retrieved

        Returns:
            Any: [description]
        """
        if self.empty():
            raise Exception("Nothing to get!")

        first = self.sentinel.next
        cur_idx = 0
        while cur_idx < index:
            first = first.next
            cur_idx += 1
        return first.val

    def is_empty(self) -> bool:
        """returns whether the Doubly Linked List is Empty

        Returns:
            bool: True if empty
        """
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
        return "".join(str_representation)
