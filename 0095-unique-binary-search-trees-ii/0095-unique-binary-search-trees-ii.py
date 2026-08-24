
class Solution:
    def generateTrees(self, n):
        
        def build(start, end):
            # No nodes
            if start > end:
                return [None]

            result = []

            # Try every value as root
            for root_val in range(start, end + 1):

                # Generate all possible left subtrees
                left_trees = build(start, root_val - 1)

                # Generate all possible right subtrees
                right_trees = build(root_val + 1, end)

                # Combine every left subtree
                # with every right subtree
                for left in left_trees:
                    for right in right_trees:

                        root = TreeNode(root_val)

                        root.left = left
                        root.right = right

                        result.append(root)

            return result

        return build(1, n)