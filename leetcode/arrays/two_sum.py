
def two_sum(nums: list[int], target: int) -> list[int]:
    """Brute force method"""
    nums_length: int = len(nums)
    for i in range(nums_length - 1):
        for j in range(i + 1, nums_length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


