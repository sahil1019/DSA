class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            ndp = {}
            for s, cnt in dp.items():
                ndp[s + num] = ndp.get(s + num, 0) + cnt
                ndp[s - num] = ndp.get(s - num, 0) + cnt
            dp = ndp

        return dp.get(target, 0)