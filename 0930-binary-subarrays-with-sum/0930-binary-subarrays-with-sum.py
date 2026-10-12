class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        freq= {0:1}

        for num in nums:
            prefix_sum += num
            required = prefix_sum - goal
            count += freq.get(required,0)

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count

        