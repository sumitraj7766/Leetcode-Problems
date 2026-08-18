class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):

            if node is None:
                return

            # Add current node
            path.append(node.val)

            # If current node is a leaf
            if node.left is None and node.right is None:

                # Check sum
                if remaining == node.val:
                    result.append(path[:])

            else:
                # Explore left
                dfs(node.left, remaining - node.val, path)

                # Explore right
                dfs(node.right, remaining - node.val, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])

        return result