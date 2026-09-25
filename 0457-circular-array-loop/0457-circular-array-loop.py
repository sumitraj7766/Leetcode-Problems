
class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        for i in range(n):
            slow = fast = i
            forward = nums[i] > 0

            while True:
                # Move slow pointer one step
                slow = (slow + nums[slow]) % n

                if nums[slow] * (1 if forward else -1) <= 0:
                    break

                # Move fast pointer two steps
                fast = (fast + nums[fast]) % n

                if nums[fast] * (1 if forward else -1) <= 0:
                    break

                fast = (fast + nums[fast]) % n

                if nums[fast] * (1 if forward else -1) <= 0:
                    break

                # Check if a cycle exists
                if slow == fast:
                    # Reject self-loop
                    if (slow + nums[slow]) % n == slow:
                        break
                    return True

            # Mark the traversed path as visited
            current = i

            while nums[current] * (1 if forward else -1) > 0:
                nxt = (current + nums[current]) % n
                nums[current] = 0
                current = nxt

        return False