from lwdsa.ds.list import SinglyLinkedList
from lwdsa.ds.list import ArrayList 
from lwdsa.ds.list import DoublyLinkedList

def test_initialization():
    d = ArrayList(capacity=3)
    assert d.size == 0
    assert len(d.array) == 3


def test_array_list():
    d = ArrayList(capacity=5)
    d.add(5)
    d.add(1)
    d.add(50)
    d.add(60)
    d.add(70)
    d.add(10)
    #intial array has been resized 
    assert len(d.array) == 10

    assert d.get(0) == 5
    assert d.get(6) is None
    assert d.get(5) == 10

    #length of dynamicarray is only 6
    assert len(d) == 6

def test_singly_linked_list():
    SLL = SinglyLinkedList()
    SLL.add_first(5)
    SLL.add_first(10)
    assert SLL.get_first() == 10
    SLL.add_first(50)
    assert SLL.get_first() == 50
    assert len(SLL) == 3
    SLL.add_last(50)
    
def test_doubly_linked_list():
    DLL = DoublyLinkedList()
    DLL.add_first(5)
    DLL.add_last(10)
    DLL.add_last(10)

    assert DLL.sentinel.next.val = 5
    assert DLL.sentinel.next.val = 5
    assert DLL.sentinel.next.val = 6



     