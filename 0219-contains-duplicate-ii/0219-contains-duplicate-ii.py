class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in last_index and i - last_index[num] <= k:
                return True

            last_index[num] = i 

        return False
       
        