# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = [float('-inf')]

        def dfs(node):

            if node is None:
                return 0 

            left = max(0 , dfs(node.left))
            right = max(0 , dfs(node.right))

            current = left + node.val + right

            ans[0] = max(ans[0] , current)

            return node.val + max(left , right)

        dfs(root)
        return ans[0]
