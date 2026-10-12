class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        length = 1
        max_length = 1

        for i in range(1 , n):
            if arr[i] == arr[i-1]:
                length = 1

            elif i >= 2 and (
                (arr[i - 2] < arr[i - 1] and arr[i - 1] > arr[i])
                or
                (arr[i - 2] > arr[i - 1] and arr[i - 1] < arr[i])):
                length += 1

            else:
                length = 2

            max_length = max(max_length, length)

        return max_length
            




