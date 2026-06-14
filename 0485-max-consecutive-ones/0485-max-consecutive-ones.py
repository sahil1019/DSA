class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cur = 0

        for x in nums:
            if x == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0

        return ans