
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Using hash map"""
    already_appear: dict = {}
    nums_array_length: int = len(nums)
    for i in range(nums_array_length):
        if nums[i] in already_appear:
            return True
        already_appear[nums[i]] = i
    return False


def contains_duplicate_set(nums: List[int]) -> bool:
    """Using python set"""
    num_set: set = set()
    for i in nums:
        if i in num_set:
            return True
        num_set.add(i)
    return False


if __name__ == "__main__":
    arr = [1, 2, 3, 1]
    print(contains_duplicate(arr))
