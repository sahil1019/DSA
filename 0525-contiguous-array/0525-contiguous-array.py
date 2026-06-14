class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pos = {0: -1}
        s = 0
        ans = 0

        for i, x in enumerate(nums):
            s += 1 if x == 1 else -1

            if s in pos:
                ans = max(ans, i - pos[s])
            else:
                pos[s] = i

        return ans