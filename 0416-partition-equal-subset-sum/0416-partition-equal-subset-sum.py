from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            dp |= {x + num for x in dp if x + num <= target}
            if target in dp:
                return True

        return False