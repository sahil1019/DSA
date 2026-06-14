from collections import Counter

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()

        def dfs(node):
            if not node:
                return 0

            s = node.val + dfs(node.left) + dfs(node.right)
            cnt[s] += 1
            return s

        dfs(root)

        mx = max(cnt.values())
        return [s for s, f in cnt.items() if f == mx]