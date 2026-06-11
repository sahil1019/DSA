from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(limit):
            count = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > limit:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num

            return count <= k

        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2

            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left