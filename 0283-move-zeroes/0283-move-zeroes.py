class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == 0:
                for j in range( i , n - 1 ):
                    nums[j] = nums[j + 1]

                nums[n - 1] = 0
                n -= 1

            else:
                i += 1
        
        