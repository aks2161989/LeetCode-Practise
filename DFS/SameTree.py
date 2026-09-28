# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return(
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )

if __name__ =="__main__":
    p = TreeNode(1, 2, 3)
    p.left = TreeNode(2, None, None)
    p.right = TreeNode(3, None, None)

    q = TreeNode(1, 2, 3)
    q.left = TreeNode(2, None, None)
    q.right = TreeNode(3, None, None)

    sol = Solution()
    print(sol.isSameTree(p, q))