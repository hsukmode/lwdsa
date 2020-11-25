"""
implementation of several sorting algorithms
"""
import concurrent
import math
import time
from typing import List, Optional


def sleep_sort(nums: List[int]) -> List[int]:
    """sleep sort algorithm introduced through 4chan
    time.sleep on input is run in a separate thread, when thread completes, it is appended to
    list.
    ##No guarantees this will return the correct result every time##

    Args:
        nums (List[int]): to swap in place requires a list of integers

    Returns:
        List[int]: potentially sorted list of nums
    """
    if len(nums) > 10:
        raise Exception("sleep sort will take too long on this input!")

    def sleep(val) -> int:
        time.sleep(val)
        return val

    sorted_results = []
    with concurrent.future.ThreadPoolExecutor() as executor:
        future_to_sort = {executor.submit(sleep, num): num for num in nums}
        for future in concurrent.futures.as_completed(future_to_sort):
            data = future.result()
            sorted_results.append(data)
    return sorted_results


def bubble_sort(nums: List[int]) -> List[int]:
    """bubble sort algorithm is implemented as follows
    keep a max value
    iterate through the list

    Time Complexity: (O(N)^2)

    Args:
        nums (List[int]): list of nums

    Returns:
        List[int]: sorted list of nums
    """
    for counter in range(len(nums)):
        for idx in range(len(nums) - 1 - counter):
            if nums[idx] > nums[idx + 1]:
                nums[idx + 1], nums[idx] = nums[idx], nums[idx + 1]

    return nums


def selection_sort(nums: List[int]) -> List[int]:
    """selection sort algorithm is implemented as follows
    start with a pointer at the beginning of the list.
    each iteration, find the minimum element by traversing
    through values and swapping with the pointer
    increase pointer by one after each iteration until you have reached end of the list.
    in a sense, it is very similiar to bubble sort

    Time Complexity: (O(N)^2)

    Args:
        nums (List[int]): list of numbers

    Returns:
        List[int]: sorted list of nums
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


def insertion_sort(nums: List[int]) -> List[int]:
    """implementation of insertation sort algorithm

    Args:
        nums (List[int]): list of nums

    Returns:
        List[int]: sorted list of nums
    """
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] > nums[j - 1]:
                break
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums


def counting_sort(
    nums: List[int], bucket_size: Optional[int] = None, exponent: int = 1
) -> List[int]:
    """counting sort creates k buckets (where values in num are within range (0, nums -1))

    Implementation based on this:
    https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/
    6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec07.pdf

    Args:
        nums (List[int]): positive list of numbers

    Returns:
        List[int]: sorted nums
    """
    if not nums:
        return nums

    if min(nums) < 0:
        raise Exception("this implementation of counting sort only takes in positive numers!")

    # differentiate for radix sort
    new_bucket_size = bucket_size if bucket_size else max(nums) + 1
    buckets = [[] for i in range(new_bucket_size)]

    for j in range(len(nums)):
        # differentiate for radix sort
        idx = (nums[j] // exponent) % 10 if bucket_size else nums[j]
        buckets[idx].append(nums[j])

    sorted_output = []
    for bucket in buckets:
        sorted_output.extend(bucket)

    return sorted_output


def radix_sort(nums: List[int]) -> List[int]:
    """Radix sort allows us to sort digits in linear time
    This implementation is the MSD version of radix sort, each digit is sorted based
    on modified version of counting sort

    Args:
        nums (List[int]):
            positive list of ints (no real constraint on input size unlike counting sort)

    Returns:
        List[int]: sorted list of numbers
    """
    if not nums:
        return nums
    max_num = max(nums)
    digits = math.floor(math.log10(max_num + 1)) + 1

    exponent = 1

    for i in range(digits):

        nums = counting_sort(nums=nums, bucket_size=10, exponent=exponent)
        exponent = exponent * 10

    return nums


def _merge(list_one: List[int], list_two: List[int]) -> List[int]:
    list_one_idx = 0
    list_two_idx = 0
    merged = []
    while list_one_idx < len(list_one) and list_two_idx < len(list_two):
        if list_one[list_one_idx] < list_two[list_two_idx]:
            merged.append(list_one[list_one_idx])
            list_one_idx += 1
        else:
            merged.append(list_two[list_two_idx])
            list_two_idx += 1

    merged.extend(list_two[list_two_idx:])
    merged.extend(list_two[list_one_idx:])

    return merged


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 0 or len(nums) == 1:
        return nums[: len(nums)]
    halfway = len(list) // 2
    list1 = list[0:halfway]
    list2 = list[halfway : len(list)]
    newlist1 = merge_sort(list1)  # recursively sort left half
    newlist2 = merge_sort(list2)  # recursively sort right half
    newlist = _merge(newlist1, newlist2)
    return newlist


def quick_sort(nums: List[int]) -> List[int]:
    pass


def heap_sort(nums: List[int]) -> List[int]:
    pass
