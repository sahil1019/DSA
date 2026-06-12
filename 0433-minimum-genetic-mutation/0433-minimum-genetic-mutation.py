from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        genes = ['A', 'C', 'G', 'T']
        q = deque([(startGene, 0)])
        visited = {startGene}

        while q:
            gene, steps = q.popleft()

            if gene == endGene:
                return steps

            gene_list = list(gene)

            for i in range(8):
                original = gene_list[i]

                for ch in genes:
                    if ch == original:
                        continue

                    gene_list[i] = ch
                    nxt = ''.join(gene_list)

                    if nxt in bank and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

                gene_list[i] = original

        return -1