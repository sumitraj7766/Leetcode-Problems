class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]

        while low < high:
            mid = (low+high)//2

            count = 0 
            for row in matrix:
                for num in row:
                    if num <= mid:
                        count += 1
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low