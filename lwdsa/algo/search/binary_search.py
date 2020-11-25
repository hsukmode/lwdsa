from typing import List, Optional, Literal


def _binary_search_recursive(nums: List[int], value: int, left: int, right: int) -> bool:
    """Recursive implementation of binary search"""
    if left > right:
        return False

    mid = (left + right) // 2

    if nums[mid] == value:
        return True

    elif nums[mid] > value:
        return _binary_search_recursive(nums, value, left, mid - 1)

    elif nums[mid] < value:
        return _binary_search_recursive(nums, value, mid + 1, right)


def _binary_search_iterative(nums: List[int], value: int) -> bool:
    """Iterative version of binary search"""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return True
        elif nums[mid] < value:
            left = mid + 1
        elif nums[mid] > value:
            right -= 1

    return False


def binary_search(
    nums, value, method: Optional[Literal["recursive", "iterative"]] = "iterative"
) -> bool:
    """binary search"""
    if method == "recursive":
        return _binary_search_recursive(nums, value, 0, len(nums) - 1)
    return _binary_search_iterative(nums, value)
