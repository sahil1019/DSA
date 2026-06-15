import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        mx = float('-inf')

        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            mx = max(mx, arr[0])

        left, right = -10**5, 10**5

        while True:
            mn, row, idx = heapq.heappop(heap)

            if mx - mn < right - left:
                left, right = mn, mx

            if idx + 1 == len(nums[row]):
                break

            nxt = nums[row][idx + 1]
            heapq.heappush(heap, (nxt, row, idx + 1))
            mx = max(mx, nxt)

        return [left, right]