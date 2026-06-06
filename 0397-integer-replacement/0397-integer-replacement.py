from functools import cache

class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dfs(x):
            if x == 1:
                return 0

            if x % 2 == 0:
                return 1 + dfs(x // 2)

            return 1 + min(
                dfs(x - 1),
                dfs(x + 1)
            )

        return dfs(n)