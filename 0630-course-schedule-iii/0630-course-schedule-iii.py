import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        total = 0
        heap = []

        for duration, lastDay in courses:
            total += duration
            heapq.heappush(heap, -duration)

            if total > lastDay:
                total += heapq.heappop(heap)

        return len(heap)