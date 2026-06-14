class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = {}

        def dfs(node):
            if not node:
                return
            cnt[node.val] = cnt.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        mx = max(cnt.values())
        return [x for x, c in cnt.items() if c == mx]