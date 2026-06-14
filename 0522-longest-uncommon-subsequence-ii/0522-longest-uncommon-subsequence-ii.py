class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a, b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)

        for i, s in enumerate(strs):
            if all(not is_subseq(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)

        return -1