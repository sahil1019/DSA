"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(r, c, size):
            first = grid[r][c]

            same = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(bool(first), True, None, None, None, None)

            half = size // 2

            return Node(
                True,
                False,
                build(r, c, half),                    # topLeft
                build(r, c + half, half),             # topRight
                build(r + half, c, half),             # bottomLeft
                build(r + half, c + half, half)       # bottomRight
            )

        return build(0, 0, len(grid))