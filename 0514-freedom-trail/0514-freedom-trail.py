from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        pos = defaultdict(list)

        for i, ch in enumerate(ring):
            pos[ch].append(i)

        n = len(ring)

        @lru_cache(None)
        def dfs(i, cur):
            if i == len(key):
                return 0

            ans = float('inf')

            for nxt in pos[key[i]]:
                diff = abs(nxt - cur)
                step = min(diff, n - diff)
                ans = min(ans, step + 1 + dfs(i + 1, nxt))

            return ans

        return dfs(0, 0)