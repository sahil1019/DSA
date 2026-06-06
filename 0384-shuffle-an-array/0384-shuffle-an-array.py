import random

class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self) -> list[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> list[int]:
        arr = self.nums[:]

        for i in range(len(arr)):
            j = random.randint(i, len(arr) - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr