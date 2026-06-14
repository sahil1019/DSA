from collections import Counter

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = Counter()

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                cnt[pos] += 1

        return len(wall) - (max(cnt.values()) if cnt else 0)