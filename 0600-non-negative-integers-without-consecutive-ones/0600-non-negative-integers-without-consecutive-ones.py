class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0] = 1
        f[1] = 2

        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]

        ans = 0
        prev_bit = 0

        for i in range(30, -1, -1):
            if n & (1 << i):
                ans += f[i]

                if prev_bit:
                    return ans

                prev_bit = 1
            else:
                prev_bit = 0

        return ans + 1