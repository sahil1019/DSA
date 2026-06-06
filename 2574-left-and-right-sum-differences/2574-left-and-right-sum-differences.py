class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left_sum = 0
        ans = []

        for num in nums:
            total -= num  # right sum
            ans.append(abs(left_sum - total))
            left_sum += num

        return ans