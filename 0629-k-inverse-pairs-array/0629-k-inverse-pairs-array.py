class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [1] + [0] * k

        for i in range(1, n + 1):
            new = [0] * (k + 1)
            prefix = 0

            for j in range(k + 1):
                prefix += dp[j]

                if j >= i:
                    prefix -= dp[j - i]

                new[j] = prefix % MOD

            dp = new

        return dp[k]