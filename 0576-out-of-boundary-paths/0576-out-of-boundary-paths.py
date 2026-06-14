class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        ans = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for _ in range(maxMove):
            ndp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if dp[i][j]:
                        for dx, dy in dirs:
                            ni, nj = i + dx, j + dy

                            if 0 <= ni < m and 0 <= nj < n:
                                ndp[ni][nj] = (ndp[ni][nj] + dp[i][j]) % MOD
                            else:
                                ans = (ans + dp[i][j]) % MOD

            dp = ndp

        return ans