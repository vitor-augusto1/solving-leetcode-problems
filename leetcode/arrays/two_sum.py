
def two_sum(nums: list[int], target: int) -> list[int]:
    """Brute force method"""
    nums_length: int = len(nums)
    for i in range(nums_length - 1):
        for j in range(i + 1, nums_length):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    """Hash table method"""
    nums_length: int = len(nums)
    hash_table: dict = {}
    for i in range(nums_length):
        complement = target - nums[i]
        if complement in hash_table:
            return [i, hash_table[complement]]
        hash_table[nums[i]] = i
    return []


if __name__ == "__main__":
    numbers: list[int] = [2, 7, 11, 15]
    target: int = 9
    result = two_sum_hash_table(numbers, target)
    print(result)
