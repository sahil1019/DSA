from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, dst, visited):
            if src == dst:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei, dst, visited)
                    if res != -1:
                        return weight * res

            return -1

        ans = []

        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set()))

        return ans