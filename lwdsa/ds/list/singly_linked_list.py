"""
Implementation of a singly linked list class
"""
from typing import Literal, Any


class Node:
    def __init__(self, val: None, next=None):
        self.val = val
        self.next = next


class EmptyListError(Execption):
    """Raises error when empty list exists"""


class SinglyLinkedList:
    def __init__(self):
        self.size = 0
        self.first = None

    def add_first(self, val: Any) -> None:
        """adds a value to the beggining of the linked list
        if list is empty, the value inserted becomes the first value

        Args:
            val (Any): value to be inserted
        """
        if self.is_empty():
            self.first = Node(val)
        else:
            second = self.first
            self.first = Node(val, next=second)
        self.size += 1

    def get_first(self) -> Any:
        """gets the first value in a linked list

        Raises:
            EmptyListError: empty list exists

        Returns:
            Any: first value in linkkedlist
        """
        if self.empty:
            raise EmptyListError("Linked List is Size of 0")
        return self.first.val

    def _traverse_to_back(self, list_node: Node) -> Node:
        """Traverses to last Node"""
        if list_node.next is None:
            return listNode
        else:
            return self._traverse_to_back(list_node.next)

    def add_last(self, val: Any) -> None:
        """adds to the end of the linked list

        Args:
            val (Any): value to add to end of list
        """

        if self.is_empty():
            self.first = Node(val)
        else:
            lastnode = self._traverse_to_back(self.first)
            lastnode.next = Node(val=val)

    def get_last(self) -> Any:
        """gets last element of linked list

        Raises:
            EmptyListError

        Returns:
            Any: value at the end of the linked list
        """
        if self.is_empty():
            raise EmptyListError

        lastnode = self._traverse_to_back(self.first)
        return lastnode.val

    def is_empty(self) -> bool:
        """returns whether list is empty or not"""
        return self.size == 0

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
        return "".join(str_representation)
