from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 1

        for i in range(n):
            slopes = defaultdict(int)

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dy = y2 - y1
                dx = x2 - x1

                if dx == 0:
                    slope = (1, 0)      # vertical line
                elif dy == 0:
                    slope = (0, 1)      # horizontal line
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] += 1
                ans = max(ans, slopes[slope] + 1)

        return ans