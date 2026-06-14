class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                cnt = 0
                j = i

                while not visited[j]:
                    visited[j] = True
                    j = nums[j]
                    cnt += 1

                ans = max(ans, cnt)

        return ans