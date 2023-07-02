from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n: int = len(nums)
    left_product = [1] * n
    right_product = [1] * n

    for i in range(1, n):
        left_product[i] = left_product[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_product[i] = right_product[i + 1] * nums[i + 1]

    result = [left_product[i] * right_product[i] for i in range(n)]
    return result


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 4]
    print(product_except_self(nums))
