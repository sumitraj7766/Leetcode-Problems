class Solution:
    def findTarget(self, root, k):

        nums = []

        # Inorder traversal
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        # Two pointers
        left = 0
        right = len(nums) - 1

        while left < right:

            total = nums[left] + nums[right]

            if total == k:
                return True

            elif total < k:
                left += 1

            else:
                right -= 1

        return False