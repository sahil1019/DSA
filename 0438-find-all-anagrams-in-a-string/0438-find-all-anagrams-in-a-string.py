from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)

        if n > m:
            return []

        need = [0] * 26
        window = [0] * 26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        for ch in s[:n]:
            window[ord(ch) - ord('a')] += 1

        ans = []

        if window == need:
            ans.append(0)

        for i in range(n, m):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i - n]) - ord('a')] -= 1

            if window == need:
                ans.append(i - n + 1)

        return ans