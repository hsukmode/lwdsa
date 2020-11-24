from typing import Callable

from lwdsa.algo.sorting import bubble_sort, selection_sort, insertion_sort, counting_sort, radix_sort





def test_sorts():
    def helper(sorting_algorithm: Callable):
        assert sorting_algorithm([]) == []
        assert sorting_algorithm([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert sorting_algorithm([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert sorting_algorithm([100, 4, 3, 2, 1]) == [1, 2, 3, 4, 100]
        assert sorting_algorithm([100, 4, 30, 2, 1]) == [1, 2, 4, 30, 100]
    
    
    map(helper, [bubble_sort, selection_sort, insertion_sort, counting_sort, radix_sort])
    
