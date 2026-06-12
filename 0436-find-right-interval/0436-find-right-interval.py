from typing import List
from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))

        ans = []

        for start, end in intervals:
            idx = bisect_left(starts, (end,))

            if idx == len(starts):
                ans.append(-1)
            else:
                ans.append(starts[idx][1])

        return ans