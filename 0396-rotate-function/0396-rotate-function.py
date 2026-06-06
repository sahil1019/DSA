class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)

        F = sum(i * num for i, num in enumerate(nums))
        ans = F

        for k in range(1, n):
            F = F + total - n * nums[-k]
            ans = max(ans, F)

        return ans