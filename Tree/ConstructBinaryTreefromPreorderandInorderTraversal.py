# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {
            value:index for index, value 
            in enumerate(inorder)
        }

        preorder_index = 0

        def build(left:int, right:int) -> optional[TreeNode]:
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]

            preorder_index += 1

            root = TreeNode(root_value)

            root_index = inorder_map[root_value]

            root.left = build(left, root_index-1)
            root.right = build(root_index+1, right)

            return root

        return build(0, len(inorder) - 1)


def print_tree(root):
    if not root:
        print([])
        return

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    # Remove unnecessary None values from the end
    while result and result[-1] == "null":
        result.pop()

    print(result)

if __name__ == "__main__":
    sol = Solution()
    print_tree(sol.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
