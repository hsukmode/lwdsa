"""
implementation of several sorting algorithms
"""
from typing import Sequence, List
from concurrent.futures import ThreadPoolExecutor



def sleep_sort(nums: List[int]) -> List[int]:
    """sleep sort algorithm introduced through 4chan
    time.sleep on input is run in a seperate thread, when thread completes, it is appended to 
    list.
    #No guarantees this will return the correct result every time

    Args:
        nums (List[int]): to swap in place requires a list of integers

    Returns:
        List[int]: potentially sorted list of initial 
    """
    if len(nums) > 10:
        raise Exception("sleep sort will take too long on this input!")

    def sleep(val) -> int:
        time.sleep(val)
        return val

    sorted_results = []
    with concurrent.future.ThreadPoolExecutor:
        future_to_url = {executor.submit(sleep, num): num for num in nums}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            data = future.result()
            sorted_results.append(data)
    return sorted_results



def bubble_sort(nums: List[int]) -> List[int]:
    """bubble sort algorithm is implemented as follows
    keep a max value
    iterate through the list

    Args:
        nums (List[int]): [description]

    Returns:
        List[int]: [description]
    """
    max_val = float('-inf')
    for idx in range(len(nums) - 1):
        if nums[idx] > nums[idx +1]:
            nums[idx + 1], nums[idx] = nums[idx], nums[idx + 1]
        else:
            nums[idx] > nums[idx +1]

        
    
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    pass

def insertion_sort(nums: List[int]) -> List[int]:
    pass


def merge_sort(nums: List[int]) -> List[int]:
    pass

def quick_sort(nums: List[int]) -> List[int]:
    pass

def counting_sort(nums: List[int]) -> List[int]:
    pass

def bucket_sort(nums: List[int]) -> List[int]:
    pass

def radix_sort(nums: List[int]) -> List[int]:
    pass


