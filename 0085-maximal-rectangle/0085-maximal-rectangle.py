class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for i in range(rows):

            # Build histogram for the current row
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Find the largest rectangle in this histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area