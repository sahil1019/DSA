class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        min_row = min(a for a, b in ops)
        min_col = min(b for a, b in ops)

        return min_row * min_col