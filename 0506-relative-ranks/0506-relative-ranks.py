class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [""] * n

        order = sorted(range(n), key=lambda i: -score[i])

        for rank, idx in enumerate(order, 1):
            if rank == 1:
                ans[idx] = "Gold Medal"
            elif rank == 2:
                ans[idx] = "Silver Medal"
            elif rank == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank)

        return ans