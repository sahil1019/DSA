from functools import cache
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        target = stones[-1]

        @cache
        def dfs(pos, jump):
            if pos == target:
                return True

            for nxt_jump in (jump - 1, jump, jump + 1):
                if nxt_jump > 0 and pos + nxt_jump in stone_set:
                    if dfs(pos + nxt_jump, nxt_jump):
                        return True

            return False

        return dfs(0, 0)