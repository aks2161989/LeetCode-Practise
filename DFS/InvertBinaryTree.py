from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        root.left, root.right = root.right, root.left


        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

def tree_to_list(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
        else:
            result.append(node.val)

            # Add both children, even if they are None
            queue.append(node.left)
            queue.append(node.right)

    # Remove unnecessary None values from the end
    while result and result[-1] is None:
        result.pop()

    return result

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))

    sol = Solution()
    result = sol.invertTree(root)
    print(tree_to_list(result))