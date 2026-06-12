class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        memo = {}

        def dfs(used, total):
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)

                if used & bit:
                    continue

                if i >= total or not dfs(used | bit, total - i):
                    memo[used] = True
                    return True

            memo[used] = False
            return False

        return dfs(0, desiredTotal)