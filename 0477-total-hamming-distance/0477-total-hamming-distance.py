class Solution:
    def totalHammingDistance(self, nums):
        n = len(nums)
        ans = 0

        for bit in range(32):
            ones = sum((num >> bit) & 1 for num in nums)
            ans += ones * (n - ones)

        return ans