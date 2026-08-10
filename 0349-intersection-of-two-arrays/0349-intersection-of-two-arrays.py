class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        result = set()

        for num in nums2:
            left = 0
            right = len(nums1) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums1[mid] == num:
                    result.add(num)
                    break

                elif nums1[mid] < num:
                    left = mid + 1

                else:
                    right = mid - 1

        return list(result)