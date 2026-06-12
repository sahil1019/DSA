# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        idx = 0

        def build(lower, upper):
            nonlocal idx

            if idx == len(vals):
                return None

            val = vals[idx]

            if val < lower or val > upper:
                return None

            idx += 1

            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)

            return node

        return build(float("-inf"), float("inf"))