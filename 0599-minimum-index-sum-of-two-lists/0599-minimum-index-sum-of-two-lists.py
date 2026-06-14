class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pos = {s: i for i, s in enumerate(list1)}
        best = float('inf')
        ans = []

        for j, s in enumerate(list2):
            if s in pos:
                idx_sum = pos[s] + j

                if idx_sum < best:
                    best = idx_sum
                    ans = [s]
                elif idx_sum == best:
                    ans.append(s)

        return ans