# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(node, minimum, maximum):
            if not node:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            return (
                dfs(node.left, minimum, node.val)
                and
                dfs(node.right, node.val, maximum)
            )

        return dfs(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.isValidBST(root))