class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        s = 1
        d = 2

        while d * d <= num:
            if num % d == 0:
                s += d
                if d * d != num:
                    s += num // d
            d += 1

        return s == num