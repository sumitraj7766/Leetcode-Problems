# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(node , current):
            if node is None:
                return 0 

            current = current * 10 + node.val

            if node.left is None and node.right is None:
                return current
            left_sum = dfs(node.left, current)
            right_sum = dfs(node.right , current)

            return left_sum + right_sum

        return dfs(root, 0)
        