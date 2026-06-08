from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []

        for h, k in people:
            queue.insert(k, [h, k])

        return queue