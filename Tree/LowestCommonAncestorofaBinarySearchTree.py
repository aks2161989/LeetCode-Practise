# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(6)

    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    sol = Solution()

    # Example 1: p = 2, q = 8
    p = root.left
    q = root.right

    result = sol.lowestCommonAncestor(root, p, q)

    print(result.val)