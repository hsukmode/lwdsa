from typing import Callable

from lwdsa.algo.sorting import bubble_sort, selection_sort, insertion_sort, counting_sort

def helper(sorting_algorithm: Callable):
        assert sorting_algorithm([]) == []
        assert sorting_algorithm([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert sorting_algorithm([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        

def test_sorts():
    
    map(helper, [bubble_sort, selection_sort, insertion_sort])
    

def test_counting_sort():
    map(helper, [counting_sort])