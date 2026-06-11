from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)

        length = 0
        odd_found = False

        for freq in cnt.values():
            length += (freq // 2) * 2
            if freq % 2:
                odd_found = True

        return length + 1 if odd_found else length