class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            count = {}

            for num in nums:
                count[num] = count.get(num, 0) + 1

            return sum(1 for freq in count.values() if freq >= 2)
        unique = set(nums)
        answer = 0

        for num in unique:
            if num + k in unique :
                answer += 1
        return answer
        