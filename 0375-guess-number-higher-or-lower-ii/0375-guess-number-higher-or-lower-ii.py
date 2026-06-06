from functools import cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dfs(left, right):
            if left >= right:
                return 0

            ans = float('inf')

            for x in range(left, right + 1):
                cost = x + max(
                    dfs(left, x - 1),
                    dfs(x + 1, right)
                )
                ans = min(ans, cost)

            return ans

        return dfs(1, n)