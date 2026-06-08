class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        chars = "0123456789abcdef"
        res = []

        # Handle negative numbers using 32-bit two's complement
        num &= 0xffffffff

        while num:
            res.append(chars[num & 15])  # num % 16
            num >>= 4

        return ''.join(reversed(res))