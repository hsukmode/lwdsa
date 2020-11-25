"""general util functions"""


def num_of_digits(num: int) -> int:
    """returns number of digits in a number

    Args:
        num (int):

    Returns:
        int: number of digits in an integer
    """
    count = 0
    while num:
        count += 1
        num //= 10
    return count
