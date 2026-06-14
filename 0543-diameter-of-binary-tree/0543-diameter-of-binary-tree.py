class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def depth(node):
            nonlocal ans
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            ans = max(ans, left + right)

            return 1 + max(left, right)

        depth(root)
        return ans