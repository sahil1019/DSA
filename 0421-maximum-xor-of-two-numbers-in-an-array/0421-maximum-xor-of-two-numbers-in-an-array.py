from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0

        for bit in range(31, -1, -1):
            mask |= (1 << bit)

            prefixes = {num & mask for num in nums}

            candidate = ans | (1 << bit)

            for p in prefixes:
                if (candidate ^ p) in prefixes:
                    ans = candidate
                    break

        return ans