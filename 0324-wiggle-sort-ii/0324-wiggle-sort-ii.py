class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        nums.sort()
        mid = (n-1) // 2

        small = nums[:mid + 1][::-1]
        large = nums[mid + 1:][::-1]

        for i in range(len(large)):
            nums[2 * i] = small[i]
            nums[2 * i + 1] = large[i]

        if n % 2 == 1:
            nums[-1] = small[-1]


        