class Solution:
    def countNodes(self, root):

        if not root:
            return 0

        # Find the height of the tree
        h = 0
        node = root

        while node.left:
            h += 1
            node = node.left

        # Check whether a node exists at index idx
        def exists(idx):
            left = 0
            right = (1 << h) - 1

            node = root

            for _ in range(h):
                mid = (left + right) // 2

                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1

                if not node:
                    return False

            return True

        # Binary search for the last existing node
        left = 0
        right = (1 << h) - 1

        while left <= right:
            mid = (left + right) // 2

            if exists(mid):
                left = mid + 1
            else:
                right = mid - 1

        # Nodes before last level + nodes on last level
        return (1 << h) - 1 + left