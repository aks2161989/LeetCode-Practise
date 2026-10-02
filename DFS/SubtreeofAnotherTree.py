# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def sameTree(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False

            return (
                sameTree(node1.left, node2.left) and
                sameTree(node1.right, node2.right)
            )

        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return(
            self.isSubtree(
                root.left, subRoot) 
                or 
                self.isSubtree(root.right, subRoot
            )
        )

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    sol = Solution()
    print(sol.isSubtree(root, subRoot))