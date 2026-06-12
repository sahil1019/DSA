from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        keep = 1

        for start, finish in intervals[1:]:
            if start >= end:
                keep += 1
                end = finish

        return len(intervals) - keep