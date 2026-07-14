class Solution(object):
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get( num , 0 ) + 1


        ans = []

        limit = len(nums) // 3
        for num, count in freq.items():

            if count > limit:
                ans.append(num)

        return ans
      