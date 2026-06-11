from heapq import heappush, heappop
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        visited = [[False] * n for _ in range(m)]
        heap = []

        # Add boundary cells
        for r in range(m):
            heappush(heap, (heightMap[r][0], r, 0))
            heappush(heap, (heightMap[r][n - 1], r, n - 1))
            visited[r][0] = True
            visited[r][n - 1] = True

        for c in range(1, n - 1):
            heappush(heap, (heightMap[0][c], 0, c))
            heappush(heap, (heightMap[m - 1][c], m - 1, c))
            visited[0][c] = True
            visited[m - 1][c] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            h, r, c = heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and not visited[nr][nc]
                ):
                    visited[nr][nc] = True

                    nh = heightMap[nr][nc]
                    water += max(0, h - nh)

                    heappush(heap, (max(h, nh), nr, nc))

        return water