import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0

        for x1, y1, x2, y2 in rects:
            total += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.prefix.append(total)

    def pick(self) -> List[int]:
        k = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, k)

        x1, y1, x2, y2 = self.rects[idx]

        return [
            random.randint(x1, x2),
            random.randint(y1, y2)
        ]