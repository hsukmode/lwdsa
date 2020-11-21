from lwdsa.ds.array import DynamicArray 


def test_initialization():
    d = DynamicArray(capacity=3)
    assert d.size == 0
    assert len(d.array) == 3


def test_dynamic_array():
    d = DynamicArray(capacity=5)
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
    
    


