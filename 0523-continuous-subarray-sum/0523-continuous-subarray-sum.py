class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        s = 0

        for i, x in enumerate(nums):
            s += x
            r = s if k == 0 else s % k

            if r in mp:
                if i - mp[r] > 1:
                    return True
            else:
                mp[r] = i

        return False