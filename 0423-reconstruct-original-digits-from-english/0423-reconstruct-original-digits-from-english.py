from typing import List
from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        digits = [0] * 10

        digits[0] = cnt['z']  # zero
        digits[2] = cnt['w']  # two
        digits[4] = cnt['u']  # four
        digits[6] = cnt['x']  # six
        digits[8] = cnt['g']  # eight

        digits[3] = cnt['h'] - digits[8]      # three
        digits[5] = cnt['f'] - digits[4]      # five
        digits[7] = cnt['s'] - digits[6]      # seven

        digits[1] = cnt['o'] - digits[0] - digits[2] - digits[4]
        digits[9] = cnt['i'] - digits[5] - digits[6] - digits[8]

        return ''.join(str(i) * digits[i] for i in range(10))