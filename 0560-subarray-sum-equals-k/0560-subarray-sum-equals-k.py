class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            ans += cnt.get(prefix - k, 0)
            cnt[prefix] = cnt.get(prefix, 0) + 1

        return ans