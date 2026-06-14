class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0

        def dfs(node):
            nonlocal tilt
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            tilt += abs(left - right)

            return node.val + left + right

        dfs(root)
        return tilt